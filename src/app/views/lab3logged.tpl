%def body():
<div class="span8">
    <h2><img src="/static/favicon.ico">Messages</h2>

    <div>
        <p>'You ought to be ashamed of yourself for asking such a simple question,' added the Gryphon;</p>

        <div>
            <span class="badge badge-success">Posted 2012-08-02 20:47:04</span>

            <div class="pull-right">
                <span class="label">alice</span>
                <span class="label">story</span>
                <span class="label">blog</span>
                <span class="label">personal</span>
            </div>
        </div>
        <hr>
    </div>

</div>

<div class="span4 well">
    <h4><i class="icon-pencil"></i> New post</h4>

    <form accept-charset="UTF-8" action="" method="POST">
        <textarea class="span12" id="message" name="message" placeholder="Type in your message" rows="5"></textarea>
        <button class="btn btn-info pull-right" type="submit">Post New Message</button>
        <p>
            <small>Use &laquo;@name&raquo; to notify some user. And &laquo;#name&raquo; to add new tag to post</small>
        </p>
    </form>
</div>
%end

%def script():
<script type="text/javascript">

</script>
%end

%rebase base body=body, script=script, title="Lab 3"
