%def body():
<div class="span6 offset3 well" style="padding: 16px 32px;">
    <legend>New to Selenium, Sign up!</legend>

    %if errors:
    <div class="alert alert-error">
        %for error in errors:
        <a class="close" data-dismiss="alert" href="#">×</a>{{ error }}<br>
        %end
    </div>
    %end

    <form method="POST" action="" accept-charset="UTF-8">
        <input type="text" id="email" class="span12" name="email" value="{{ email }}" placeholder="Email">
        <input type="text" id="username" class="span12" name="username" value="{{ username }}" placeholder="Username">
        <input type="password" id="password" class="span12" name="password" placeholder="Password">
        <button type="submit" name="submit" class="btn btn-info btn-block">Sign up</button>
    </form>
</div>
%end

%def script():
<script type="text/javascript">
    jQuery('#email').focus();
</script>
%end

%rebase base body=body, script=script, title="Lab 3 - Sign Up"
