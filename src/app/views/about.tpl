%def body():
<div class="span12" style="text-align: center;">
    <p>
        It is simple web application for testing purpose with selenium tool.<br>
        It is written with python <a href="http://bottlepy.org/">bottle</a> mini framework,
        and twitter <a href="http://twitter.github.com/bootstrap/">bootstrap</a> front-end framework.
    </p>

    <p>
        Source code you can find on <a href="https://bitbucket.org/b7w/seleniumhowto">bitbucket.org</a>,
        with <a href="https://bitbucket.org/b7w/seleniumhowto/src/default/docs?at=default">how to</a>.
        Dependencies are already included.<br>
        All code running on python 3. <em>Note, selenium library is ported to third version.</em><br>
    </p>

    <p>
        Feel free to contact me via email <a href="mailto:black7white@ya.ru">black7white@ya.ru</a><br>
        Be not lazy to send bugs to
        <a href="https://bitbucket.org/b7w/seleniumhowto/issues?status=new&status=open">issues tracker</a>
    </p>
</div>
%end

%rebase base body=body, title="About"
