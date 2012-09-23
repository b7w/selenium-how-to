%def body():
<div class="span5">
    <h3><img src="/static/favicon.ico"> Striped bars</h3>

    <p>Similar to the solid colors, we have varied striped progress bars.</p>

    <div class="progress progress-info progress-striped active" style="margin-bottom: 9px;">
        <div id="progress1" class="bar" style="width: 0%"></div>
    </div>

    <div class="progress progress-success progress-striped active" style="margin-bottom: 9px;">
        <div id="progress2" class="bar" style="width: 0%"></div>
    </div>
    <div class="progress progress-warning progress-striped active" style="margin-bottom: 9px;">
        <div id="progress3" class="bar" style="width: 0%"></div>
    </div>
    <div class="progress progress-danger progress-striped active" style="margin-bottom: 9px;">
        <div id="progress4" class="bar" style="width: 0%"></div>
    </div>

</div>

<div class="span7">
    <h3><img src="/static/favicon.ico"> Controls</h3>

    <form class="form-horizontal" action="" method="post">
        <fieldset>
            <div class="control-group">
                <label class="control-label" for="input01">Text input</label>

                <div class="controls">
                    <input name="in1" type="text" class="input-xlarge" id="input01">

                    <p class="help-block">In addition to freeform text, any HTML5 text-based input appears like so.</p>
                </div>
            </div>
            <div class="control-group">
                <label class="control-label" for="optionsCheckbox">Checkbox</label>

                <div class="controls">
                    <label class="checkbox">
                        <input name="in2" type="checkbox" id="optionsCheckbox">
                        Option one is this and that—be sure to include why it's great
                    </label>
                </div>
            </div>
            <div class="control-group">
                <label class="control-label" for="select01">Select list</label>

                <div class="controls">
                    <select name="in3" id="select01">
                        <option>something</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                    </select>
                </div>
            </div>
            <div class="control-group">
                <label class="control-label" for="multiSelect">Multicon-select</label>

                <div class="controls">
                    <select name="in4" multiple="multiple" id="multiSelect">
                        <option>something</option>
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                    </select>
                </div>
            </div>
            <div class="control-group">
                <label class="control-label" for="fileInput">File input</label>

                <div class="controls">
                    <input name="in5" class="input-file" id="fileInput" type="file">
                </div>
            </div>
            <div class="control-group">
                <label class="control-label" for="textarea">Textarea</label>

                <div class="controls">
                    <textarea name="in6" class="input-xlarge" id="textarea" rows="3"></textarea>
                </div>
            </div>
            <div class="controls 2form-actions">
                <a id="save" href="/lab2/saved/" class="btn disabled">Save</a>
                <a id="cancel" href="/lab2/" class="btn">Cancel</a>
            </div>
        </fieldset>
    </form>
</div>
%end

%def script():
<script type='text/javascript'>
    var active = { 1:0, 2:0, 3:0, 4:0 };

    function activate_btn() {
        if (active[1] == 100 && active[2] == 100 && active[3] == 100 && active[4] == 100)
            jQuery('#save').removeClass('disabled');
        else
            jQuery('#save').addClass('disabled');
    }


    function changeInput1() {
        var text = jQuery.trim(jQuery('#input01').val());
        var progress = jQuery('#progress1');
        var len = text.length;
        if (len < 5) {
            progress.css('width', (20 * len) + '%');
            active[1] = 20 * len;
        }
        else {
            progress.css('width', '100%');
            active[1] = 100;
        }
        activate_btn();
    }

    function changeSelect() {
        var points = 0;
        var progress = jQuery('#progress2');
        var selected = jQuery("#select01 option:selected").text();
        if (selected != "something") points = 2;

        var len = jQuery("#multiSelect option:selected").length;
        if (len < 3)
            points = points + len;
        else
            points = points + 3;
        progress.css('width', ( 20 * points) + '%');
        active[2] = 20 * points;
    }

    function changeFile() {
        var progress = jQuery('#progress3');
        progress.css('width', '100%');
        active[3] = 100;
        activate_btn();
    }

    function changeTextArea() {
        var text = jQuery.trim(jQuery('#textarea').val());
        var progress = jQuery('#progress4');
        var len = text.length;
        if (len < 100) {
            progress.css('width', len + '%');
            active[4] = len;
        }
        else {
            progress.css('width', '100%');
            active[4] = 100;
        }
        activate_btn();
    }

    jQuery('#input01').keyup(function () {
        changeInput1();
    });

    jQuery("#select01").change(function () {
        changeSelect();
        activate_btn();
    });

    jQuery("#multiSelect").change(function () {
        changeSelect();
        activate_btn();
    });

    jQuery("#fileInput").change(function () {
        changeFile();
    });

    jQuery('#textarea').keyup(function () {
        changeTextArea();
    });

    jQuery('#save').click(function (e) {
        var btn = jQuery(this);
        if (btn.hasClass('disabled')) {
            e.preventDefault();
        }
    });
</script>
%end

%rebase base body=body, script=script, title="Lab 2"