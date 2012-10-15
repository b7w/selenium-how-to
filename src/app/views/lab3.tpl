%def body():
<div class="span4 offset4">

    <div class="well">
        <a href="/lab3/signup/" class="btn btn-block btn-primary">
            <i class="icon-flag icon-white"></i><br>
            <span style="white-space:nowrap;"><strong>Sing Up</strong></span>
        </a>

        <a href="/lab3/login/" class="btn btn-block btn-primary">
            <i class="icon-user icon-white"></i><br>
            <span style="white-space:nowrap;"><strong>Sing In</strong></span>
        </a>
    </div>

</div>
%end

%def script():
<script type="text/javascript">

</script>
%end

%rebase base body=body, script=script, title="Lab 3"
