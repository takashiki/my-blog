+++
title= "Spring Boot 中自定义 MessageConverter"
draft = false
date= "2019-03-01 14:46:10"
+++

### 背景

Spring MVC 自带比较强大的消息格式转化能力，它内部默认支持将接口返回值根据请求 header 中的 Accept 字段的值将结果转化为 纯文本、xml、json 等格式。

但是现在 web 开发和前端交互的过程中基本只会用到 json 格式，在默认配置下，浏览器直接访问接口时，由于浏览器请求 header 中会默认加上 `Accept: text/html,application/xhtml+xml,application/xml`，所以接口会返回 xml 格式的数据，导致我们的前端同学十分反感。

### 解决方案

一开始我们找到的解决方案都是只能在每个接口的 `RequestMapping` 注解里加上 `produces` 指定返回的格式，或者自定义一个 `JsonRequestMapping` 注解，这些都无法全局生效，不是特别方便和优雅。

后来参考了一篇文章，看了下 `RequestMappingHandlerAdapter` 类的源码，大概知道了 Spring MVC 消息格式自动转化的原理，然后顺着这个思路找了下自定义 MessageConverter 的方法。

最终的实现方案就是写一个 `WebConfiguration` 类，在 `extendMessageConverters` 方法中把其他 converter 都清掉，只留一个 json 的 converter，虽然也不算很优雅。示例代码如下：

```java
package com.demo;

import org.springframework.context.annotation.Configuration;
import org.springframework.http.converter.HttpMessageConverter;
import org.springframework.http.converter.json.MappingJackson2HttpMessageConverter;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

import java.util.List;

/**
 * @author zhangzhoufei
 */
@Configuration
public class WebConfiguration implements WebMvcConfigurer {

    @Override
    public void extendMessageConverters(List<HttpMessageConverter<?>> converters) {
        converters.clear();
        //具体保留哪个 json converter 要看项目中依赖的 json 组件是哪一个
        MappingJackson2HttpMessageConverter converter = new MappingJackson2HttpMessageConverter();
        converters.add(converter);
    }
}

```

非 spring boot 的项目中可以通过配置 `<mvc:annotation-driven/>` 来实现同样的效果。

### 参考文档

- [SpringMVC关于json、xml自动转换的原理研究](https://www.cnblogs.com/fangjian0423/p/springMVC-xml-json-convert.html)
- [Spring Boot：定制HTTP消息转换器](https://www.jianshu.com/p/ffe56d9553fd)
- [SpringBoot配置类WebMvcConfigurerAdapter](https://segmentfault.com/a/1190000011420942)