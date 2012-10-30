%def body():
<div class="span8">
    <h2><img src="/static/favicon.ico">Input messages</h2>

    <div id='messages'>
        %for mess in messages:
        <div id="message{{ mess.id }}" class="message">
            <div class="pull-right ">
                %if user in mess.users_notify:
                <a href="/example3/message/read/{{ mess.id }}/"><i class="icon-ok" title="Check message as read"></i></a>
                %end
                <a href="/example3/message/remove/{{ mess.id }}/"><i class="icon-remove" title="Remove message"></i></a>
            </div>

            <p class="message-body">{{ mess.message }}</p>

            <div class="info-panel">
                %if user in mess.users_notify:
                <span class="label label-info">New</span>
                %end
                %if mess.owner == user:
                <span class="user-from label label-info">Mine</span>
                %else:
                <span class="user-from label label-success">{{ mess.owner.name }}</span>
                %end
                <span class="time label label">{{ mess.time.strftime('%c') }}</span>

                <div class="tags pull-right">
                    %for tag in mess.tags:
                    <span class="badge badge-info">{{ tag }}</span>
                    %end
                </div>
            </div>
            <hr>
        </div>
        %end
    </div>

</div>

<div class="span4 well">
    <h4><i class="icon-pencil"></i> New post</h4>

    <form accept-charset="UTF-8" action="/example3/message/create/" method="POST">
        <textarea class="span12" id="post" name="message" placeholder="Type in your message" rows="5"></textarea>
        <button class="btn btn-info pull-right" id="submit" type="submit">Post New Message</button>
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

%rebase base body=body, script=script, title="Example 3 User home", user=user, newsCount=newsCount
