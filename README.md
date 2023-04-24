# PDF_split_GUI
<b>CSDN上看到的一个PDF分割的GUI脚本，使用简单，在此留存和分享。</b><br>
<div>
  <p>代码来源：（有略微的非实质性的修改）</p>
  <a href="https://blog.csdn.net/u013185349/article/details/126383855">Python脚本分割PDF文件</a>
</div>
<br>
<div id="tips">
  <h>SOME TIPS:</h><br><br>
  <span id="tip1">
    <p>TIP1--</p>
    <img src="AssertionError.jpg">
    <p>出现这个问题是文件页码超出范围但由于各种原因可以点击执行分割命令，但是无法完成分割操作并报错AssertionError，根据报错信息，只要找到错误来源文件，将assert start>=last_end这一条注释掉即可，为了防止出现其他问题，完成分割后应当恢复这一条命令。</p>
  </span>
<div>
