%def body():
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <p>Donec id elit non mi <a href="/example1/porta1/" class="label label-success">porta 1</a> gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
        tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
        Etiam porta sem malesuada magna mollis euismod. <a href="/example1/donec2/" class="label">Donec 2</a> sed odio dui.
    </p>

    <p><a class="btn" href="/example1/button1/">Button 1</a></p>
</div>
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <p>Donec id elit non mi porta gravida at eget metus. <a href="/example1/fusce3/" class="label label-important">Fusce 3</a> dapibus, tellus ac cursus commodo,
        tortor mauris condimentum nibh, ut <a href="/example1/fermentum4/" class="label label-inverse">fermentum 4</a> massa justo sit amet risus.
        Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui.
    </p>

    <p><a class="btn" href="/example1/button2/">Button 2</a></p>
</div>
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <p>Donec <a href="/example1/id5/" class="label label-info">id 5</a> elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
        tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
        <a href="/example1/etiam6/" class="label label-warning">Etiam 6</a> porta sem malesuada magna mollis euismod. Donec sed odio dui.
    </p>

    <p><a class="btn" href="/example1/button3/">Button 3</a></p>
</div>
%end

%rebase base body=body, title="Example 1"
