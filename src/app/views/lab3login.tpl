%def body():
<div class="span6 offset3 well" style="padding: 16px 32px;">
    <legend>Please Sign In</legend>

    %if error:
    <div class="alert alert-error">
        <a class="close" data-dismiss="alert" href="#">×</a>Incorrect Username or Password!
    </div>
    %end

    <form method="POST" action="" accept-charset="UTF-8">
        <input type="text" id="username" class="span12" name="username" value="{{ username }}" placeholder="Username">
        <input type="password" id="password" class="span12" name="password" placeholder="Password">
        <button type="submit" name="submit" class="btn btn-info btn-block">Sign in</button>
    </form>
</div>
%end


%def script():
<script type="text/javascript">
    jQuery('#username').focus();
</script>
%end

%rebase base body=body, script=script, title="Lab 3 - Sign In"
