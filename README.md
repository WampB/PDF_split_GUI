# PDF_tools
<h>搜集/编写的PDF小工具，部分有GUI。</h>
<h1 id="tool1">TOOL1：分割PDF——PDF_split_GUI.py</h1>
<h2 id="mentory1">CSDN上看到的一个PDF分割的GUI脚本，使用简单，在此留存和分享。</h2>
<div>
  <p>代码来源：<a href="https://blog.csdn.net/u013185349/article/details/126383855">Python脚本分割PDF文件</a>（有略微的非实质性的修改）</p>
</div>
<div id="tips">
  <h>SOME TIPS:</h>
  <span>
    <p>TIP1--</p>
    <img src="AssertionError.jpg">
    <p>出现这个问题是文件页码超出范围但由于各种原因可以点击执行分割命令，但是无法完成分割操作并报错AssertionError，根据报错信息，只要找到错误来源文件，将assert start>=last_end这一条注释掉即可，为了防止出现其他问题，完成分割后应当恢复这一条命令。</p>
  </span>
<div>
<h1 id="tool2">TOOL2：将一个文件夹中的[特定的]图片合称为PDF——PDF_combine_GUI.py</h1>
<h2 id="mentory2">按需求将图片[集合]转为PDF，更方便保存和传输。</h2>
<div>
  <p>代码来源：自主编写。</p>
</div>
