%def body():
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <p>Donec id elit non mi porta 1 gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
        tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
        Etiam porta sem malesuada magna mollis euismod. Donec 2 sed odio dui.
    </p>

    <p><a class="btn" href="#">Button 1</a></p>
</div>
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <input id="text" name="find" class="span4" type="text">

    <span id="buffer" style="font-size: 10px;">0</span>

    <p>
        <button class="btn btn-calc" id="num7" href="#">7</button>
        <button class="btn btn-calc" id="num8" href="#">8</button>
        <button class="btn btn-calc" id="num9" href="#">9</button>
        <button class="btn btn-calc" id="del" href="#">/</button>
        <button class="btn btn-calc" id="clear" href="#">C</button>
    </p>

    <p>
        <button class="btn btn-calc" id="num4">4</button>
        <button class="btn btn-calc" id="num5">5</button>
        <button class="btn btn-calc" id="num6">6</button>
        <button class="btn btn-calc" id="mul">*</button>
    </p>

    <p>
        <button class="btn btn-calc" id="num1">1</button>
        <button class="btn btn-calc" id="num2">2</button>
        <button class="btn btn-calc" id="num3">3</button>
        <button class="btn btn-calc" id="min">-</button>
    </p>

    <p>
        <button class="btn btn-calc" id="num0">0</button>
        <button class="btn btn-calc" id="plus">+</button>
        <button class="btn btn-calc" id="equal">=</button>
        <button class="btn btn-calc" id="point">.</button>
    </p>

</div>
<div class="span4">
    <h2><img src="/static/favicon.ico">Heading</h2>

    <p>Donec id 5 elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo,
        tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.
        Etiam 6 porta sem malesuada magna mollis euismod. Donec sed odio dui.
    </p>

    <p><a class="btn" href="#">Button 3</a></p>
</div>
<style type="text/css">
    .btn-calc {
        padding: 10px 14px;
        font-size: 32px;
    }
</style>
%end

%def script():
<script type="text/javascript">
    var val1 = '';
    var val2 = '';
    var operator = '';
    var flag = true;

    function flag_next() {
        flag = false;
        jQuery('#buffer').text(val1);
        jQuery('#text').val('');
    }

    function btn_calc(i) {
        jQuery('#num' + i).click(function (e) {
            if (flag) {
                val1 = val1 + i;
                jQuery('#text').val(val1);
            } else {
                val2 = val2 + i;
                jQuery('#text').val(val2);
            }
        });
    }

    for (var i = 0; i < 10; i++) {
        btn_calc(i);
    }

    jQuery('#point').click(function (e) {
        if (flag) {
            val1 = val1 + '.';
            jQuery('#text').val(val1);
        } else {
            val2 = val2 + '.';
            jQuery('#text').val(val2);
        }
    });

    jQuery('#plus').click(function (e) {
        flag_next();
        operator = '+';
    });

    jQuery('#min').click(function (e) {
        flag_next();
        operator = '-';
    });

    jQuery('#del').click(function (e) {
        flag_next();
        operator = '/';
    });

    jQuery('#mul').click(function (e) {
        flag_next();
        operator = '*';
    });

    jQuery('#clear').click(function (e) {
        val1 = "";
        val2 = "";
        flag = true;
        jQuery('#text').val('');
        jQuery('#buffer').text('0');
    });

    jQuery('#equal').click(function (e) {
        var tmp;
        if (operator == '+') {
            tmp = parseFloat(val1) + parseFloat(val2);
        } else if (operator == '-') {
            tmp = parseFloat(val1) - parseFloat(val2);
        } else if (operator == '*') {
            tmp = parseFloat(val1) * parseFloat(val2);
        } else if (operator == '/') {
            tmp = parseFloat(val1) / parseFloat(val2);
        }
        val1 = tmp;
        val2 = '';
        jQuery('#text').val(tmp);
        jQuery('#buffer').val(tmp);
    });
</script>
%end

%rebase base body=body, script=script, title="Lab 3"
