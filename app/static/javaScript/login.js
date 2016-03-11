function set_openid(openid, pr)
{
    var u = openid.search('<username>');
    if (u != -1){
        user = prompt('Enter your ' + pr + ' username:');
        openid = openid.substr(0, u) + user;
    }
    form = document.forms['login'];
    form.elements['openId'].value = openid;
}