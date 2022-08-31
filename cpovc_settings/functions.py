from cpims.emails import send_email


def report_bug(request, icode=0):
    """Method to report bugs."""
    try:
        msg = ""
        if icode == 500:
            ititle = request.POST.get('issue-500-title')
            idetail = request.POST.get('issue-500-details')
            url = request.POST.get('issue-500-url')
        else:
            ititle = request.POST.get('issue-title')
            idetail = request.POST.get('issue-details')
            url = request.POST.get('issue-url')
        msg += ititle + "\n" + "URL : %s\r" % (url) + idetail + "\n"
        # Telegram Alert
        # resp = send_message(msg)
        # Email to Service Desk and copy logged in user
        emails = ['nmugaya@gmail.com', 'help@cpims.on.spiceworks.com']
        tmsg = "CPIMS bug reporting \n URL : %s\r" % (url) + idetail + "\n"
        params = {'subject': ititle}
        hmsg = None
        for email in emails:
            send_email(email, tmsg, hmsg, params)
        resp = {'ok': True}
        tmsg = ' and Telegram' if resp['ok'] else ''
        print(msg, resp)
        response = {"message": "Service Desk%s" % (tmsg)}
    except Exception as e:
        raise e
    else:
        return response
