+++
title= "Spring-Boot Jpa 踩坑记录"
draft = false
date= "2019-05-28 20:58:28"
+++

### 与 lombok 配合使用的问题

如果 Entity 直接使用 `@Data` 注解的话，如果 Entity 之间存在关联关系，则会产生 StackOverflow 的问题。

产生这个问题的原因是 lombok 默认自动生成的 `toString()` 方法和 `hashCode` 方法会产生循环依赖。

解决方案就是只用 `@Getter`、`@Setter` 注解，然后自己重写 `toString()` 和 `hashCode` 方法。或者使用 `@EqualsAndHashCode` 注解时，在依赖的被维护端字段加上 `@EqualsAndHashCode.Exclude` 注解，也就是凡是关系注解里有 `mappedBy` 的都要加上 `@EqualsAndHashCode.Exclude`。

参考文档：

- [使用Hibernate、JPA、Lombok遇到的有趣问题](https://juejin.im/post/5b3ca5386fb9a04fd34370d2)
- [Lombok.hashCode issue with “java.lang.StackOverflowError: null”](https://stackoverflow.com/questions/34972895/lombok-hashcode-issue-with-java-lang-stackoverflowerror-null)
- [@EqualsAndHashCode](https://projectlombok.org/features/EqualsAndHashCode)

### ManyToMany 关系的关联表含有其他字段的情况

这种情况下中间表需要一个单独的 Entity 进行维护，可以考虑把 ManyToMany 转成 ManyToOne 和 OneToMany 进行维护。

参考文档：

- [The best way to map a many-to-many association with extra columns when using JPA and Hibernate](https://vladmihalcea.com/the-best-way-to-map-a-many-to-many-association-with-extra-columns-when-using-jpa-and-hibernate/)
- [JPA and Hibernate Many To Many Extra Columns Relationship Mapping Example with Spring Boot and MySQL](https://hellokoding.com/jpa-many-to-many-extra-columns-relationship-mapping-example-with-spring-boot-maven-and-mysql/)

### 如何自动维护记录创建更新信息

- `Application` 类上加上 `@EnableJpaAuditing` 
- 对应 Entity 上加上 `@EntityListeners(AuditingEntityListener.class)`
- 对应的四个字段使用注解 `@CreatedDate/@CreatedBy/@LastModifiedDate/@LastModifiedBy`
- 新增一个 `@Configuration` 类实现 `AuditorAware` 接口