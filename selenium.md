# Selenium-语法

#### selenium的开始--webdriver

如果看到这里，你需要知道怎么安装自动化测试需要的环境的话，这么来就OK了。

```text
pip install selenium
```

关于驱动不知道哪里下载的，可以访问

> Chromedriver\(Chrome\):[https://sites.google.com/a/chromium.org/chromedriver/home](https://sites.google.com/a/chromium.org/chromedriver/home)
>
> geckodriver\(Firefox\):[https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)
>
> IEDriverServer\(IE\):[http://selenium-release.storage.googleapis.com/index.html](http://selenium-release.storage.googleapis.com/index.html)
>
> operadriver\(Opera\):[https://github.com/operasoftware/operachromiumdriver/releases](https://github.com/operasoftware/operachromiumdriver/releases)

把对应的驱动下载放到python3的安装目录下就OK了。不过，这只是局限于本地的调试使用，后面部署到服务器中，还是推荐使用无头浏览器来完成自动化测试。

在写Selenium的代码之前，我们都需要导入Selenium的webdriver，这是最开始的第一步。

```text
from selenium import webdriver
```

之后，就可以使用selenium了。定义需要启动的浏览器。

```text
driver = webdriver.Chrome() //打开Chrome浏览器
driver = webdriver.Firefox() //打开Firefox浏览器
driver = webdriver.Ie() //打开IE浏览器
```

访问需要测试页面。

```text
driver.get("test url")  //test url为需要传进去的url
```

实现上面的步骤就已经可以正常打开需要测试的页面了。接下来就是对页面进行操作了，这也是Selenium强大的其中一点，各种API给开发者更容易了解。

#### selenium定位元素--find\_element

8种定位元素，可以根据页面元素的不同，使用不同的方法：

<table>
  <thead>
    <tr>
      <th style="text-align:left">&#x65B9;&#x6CD5;</th>
      <th style="text-align:left">&#x4F7F;&#x7528;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">ID&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_id()</td>
    </tr>
    <tr>
      <td style="text-align:left">name&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_name()</td>
    </tr>
    <tr>
      <td style="text-align:left">classname&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_class()</td>
    </tr>
    <tr>
      <td style="text-align:left">tag&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_tag_name()</td>
    </tr>
    <tr>
      <td style="text-align:left">text&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_text()</td>
    </tr>
    <tr>
      <td style="text-align:left">partial link text&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">driver.find_element_by_partial_link_text()</td>
    </tr>
    <tr>
      <td style="text-align:left">xpath&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">
        <p>driver.find_element_by_xpath()</p>
        <ol>
          <li>&#x7EDD;&#x5BF9;&#x8DEF;&#x5F84;&#xFF1A;find_element_by_xpath(&quot;&#x7EDD;&#x5BF9;&#x8DEF;&#x5F84;&quot;)</li>
          <li>&#x5143;&#x7D20;&#x5C5E;&#x6027;&#xFF1A;find_element_by_xpath(&quot;//input[@id=&apos;kw&apos;]&quot;)</li>
          <li>&#x5C42;&#x7EA7;&#x4E0E;&#x5C5E;&#x6027;&#x7ED3;&#x5408;&#xFF1A;find_element_by_xpath(&quot;//form[@id=&apos;login&apos;]/ul/input&quot;)</li>
          <li>&#x903B;&#x8F91;&#x8FD0;&#x7B97;&#x7B26;&#xFF1A;find_element_by_xpath(&quot;//input[@id=&apos;kw&apos;
            and@class=&apos;s_ipt&apos;]&quot;)</li>
          <li>&#x591A;&#x5143;&#x7D20;&#x7EC4;&#x5408;&#xFF1A;find_element_by_xpath(&quot;//*[@id=&apos;kw&apos;
            and @cotains=&quot;value&quot;]</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">css&#x5B9A;&#x4F4D;</td>
      <td style="text-align:left">
        <p>driver.find_element_by_css_selector()</p>
        <ol>
          <li>&#x5143;&#x7D20;&#x4E3A;ID&#x5C31;&#x4F7F;&#x7528;&#xFF1A;&#x201C;#id&#x201C;</li>
          <li>&#x5143;&#x7D20;&#x4E3A;classname&#x5C31;&#x4F7F;&#x7528;&#xFF1A;&#x201C;.classname&#x201C;</li>
          <li>data&#x6570;&#x636E;&#x5B9A;&#x4F4D;&#xFF1A;&#x201C;[data_select=&apos;data_value&apos;]&#x201C;</li>
        </ol>
      </td>
    </tr>
  </tbody>
</table>用css定位的方式是很多人都在使用的，因为在做自动化测试，主要就是操作前端DOM树的结构去定位，所以，在使用css的方法上会对DOM结构会更加了解。至于xpath也是推荐的，很多人说xpath的方法在性能上会比其他的慢，你使用之后，就会发现，差别并不是很大。

#### selenium的操作--driver.action\(\)

<table>
  <thead>
    <tr>
      <th style="text-align:left">&#x52A8;&#x4F5C;</th>
      <th style="text-align:left">&#x65B9;&#x6CD5;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">&#x70B9;&#x51FB;</td>
      <td style="text-align:left">driver.find_element(*loc).click()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x786E;&#x8BA4;&#x70B9;&#x51FB;</td>
      <td style="text-align:left">driver.find_element(*loc).submit()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x8F93;&#x5165;&#x6587;&#x672C;</td>
      <td style="text-align:left">driver.find_element(*loc).send_keys(&quot;value&quot;)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x6E05;&#x9664;&#x6587;&#x672C;</td>
      <td style="text-align:left">driver.find_element(*loc).clear()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x663E;&#x793A;&#x7B49;&#x5F85;</td>
      <td style="text-align:left">WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,&apos;value&apos;)))</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x9690;&#x5F0F;&#x7B49;&#x5F85;</td>
      <td style="text-align:left">driver.implicitly_wait(seconds)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x5F3A;&#x884C;&#x7B49;&#x5F85;</td>
      <td style="text-align:left">time.sleep(seconds)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x8868;&#x5355;&#x5207;&#x6362;</td>
      <td style="text-align:left">driver.switch_to.frame()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x7A97;&#x53E3;&#x5207;&#x6362;</td>
      <td style="text-align:left">driver.switch_to.window()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x5F39;&#x7A97;&#x5904;&#x7406;</td>
      <td style="text-align:left">
        <p>&#x70B9;&#x51FB;&#x5F39;&#x7A97;&#xFF1A;alert = driver.switch_to.alert</p>
        <p>alert.accept()</p>
        <p>&#x83B7;&#x53D6;&#x7A97;&#x53E3;&#x5185;&#x5BB9;&#xFF1A;alert.text()</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">&#x83B7;&#x53D6;title</td>
      <td style="text-align:left">driver.title</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x83B7;&#x53D6;&#x6587;&#x672C;</td>
      <td style="text-align:left">driver.find_element(*loc).text</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x83B7;&#x53D6;&#x5C5E;&#x6027;&#x503C;</td>
      <td style="text-align:left">driver.find_element(*loc).get_attribute(name)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x5173;&#x95ED;&#x6D4F;&#x89C8;&#x5668;</td>
      <td style="text-align:left">driver.close()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x5173;&#x95ED;&#x7A97;&#x53E3;</td>
      <td style="text-align:left">driver.quit()</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x9875;&#x9762;&#x622A;&#x56FE;</td>
      <td style="text-align:left">driver.get_screenshot_as_file(imageName)</td>
    </tr>
  </tbody>
</table>#### selenium的Action事件

这个事件的操作也可以在一些情况下，操作变得简单。

首先就是导入Action的库

```python
from selenium.webdriver.common.action_chains import ActionChains
```

<table>
  <thead>
    <tr>
      <th style="text-align:left">&#x52A8;&#x4F5C;</th>
      <th style="text-align:left">&#x65B9;&#x6CD5;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">&#x9F20;&#x6807;&#x53F3;&#x51FB;</td>
      <td style="text-align:left">
        <p>element=driver.find_element_by_css_selector(&quot;#kw&quot;)</p>
        <p>ActionChains(driver).context_click(element).perform()</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">&#x9F20;&#x6807;&#x53CC;&#x51FB;</td>
      <td style="text-align:left">
        <p>element=driver.find_element_by_css_selector(&quot;#kw&quot;)</p>
        <p>ActionChains(driver).double_click(DoubleClick).perform()</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">&#x9F20;&#x6807;&#x60AC;&#x505C;</td>
      <td style="text-align:left">
        <p>element=driver.find_element_by_css_selector(&quot;#kw&quot;)</p>
        <p>ActionChains(driver).move_to_element(DoubleClick).perform()</p>
      </td>
    </tr>
  </tbody>
</table>#### JS 操作

<table>
  <thead>
    <tr>
      <th style="text-align:left">&#x52A8;&#x4F5C;</th>
      <th style="text-align:left">&#x65B9;&#x6CD5;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">&#x6267;&#x884C;js</td>
      <td style="text-align:left">driver.extcute_javascript(js)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x6EDA;&#x52A8;&#x9875;&#x9762;</td>
      <td style="text-align:left">js = &quot;window.scrollTo(100,450);&quot;
        <br />driver.execute_script(js)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x6EDA;&#x52A8;&#x5230;&#x9876;&#x90E8;</td>
      <td style="text-align:left">js = &quot;window.scrollTo(0,0);&quot;
        <br />driver.execute_script(js)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x6EDA;&#x52A8;&#x5230;&#x5E95;&#x90E8;</td>
      <td style="text-align:left">js = &quot;window.scrollTo(0,document.body.scrollHeight);&quot;
        <br />driver.execute_script(js)</td>
    </tr>
    <tr>
      <td style="text-align:left">&#x6EDA;&#x52A8;&#x5230;&#x6307;&#x5B9A;&#x4F4D;&#x7F6E;</td>
      <td style="text-align:left">
        <p>target = drvier.find_element(*loc)</p>
        <p>driver.execute_script(&quot;arguments[0].scrollIntoView();&quot;,target)</p>
      </td>
    </tr>
  </tbody>
</table>现在对于上面的知识点不需要完全熟悉，只要知道selenium可以解决日常的大部分问题就可以了，还有知道怎么用就差不多了，因为你会在后面实战的时候，会用到很多方法。

