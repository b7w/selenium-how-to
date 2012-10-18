%def body():
<div class="span8">
    <h2><img src="/static/favicon.ico">Messages</h2>

    %for mess in messages:
    <div>
        <p class="message">{{ mess.message }}</p>

        <div>
            <span class="user label label-success">{{ mess.owner.name }}</span>
            <span class="time label label">{{ mess.time.strftime('%c') }}</span>

            <div class="pull-right">
                %for tag in mess.tags:
                <span class="badge badge-info">{{ tag }}</span>
                %end
            </div>
        </div>
        <hr>
    </div>
    %end

</div>

<div class="span4 well">
    <h4><i class="icon-pencil"></i> New post</h4>

    <form accept-charset="UTF-8" action="/lab3/post/" method="POST">
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
    for (var i = 0; i <= jQuery('.message').size(); i++) {
        var list = jQuery(jQuery('.message').get(i)).text().split(' ');
        for (var j = 0; j < list.length; ++j) {
            if (list[j][0] == '@') {
                list[j] = '<span class="label label-success label-light">' + list[j] + '</span>';
            }
            if (list[j][0] == '#') {
                list[j] = '<span class="badge badge-info label-light">' + list[j] + '</span>';
            }
        }
        jQuery(jQuery('.message').get(i)).html(list.join(' '));
    }

</script>
%end

%rebase base body=body, script=script, title="Lab 3"
