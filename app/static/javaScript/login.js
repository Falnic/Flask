function set_openid(openid, provider)
{
    var u = openid.search('<username>');
    if (u != -1){
        user = prompt('Enter your ' + provider + ' username:');
        openid = openid.substr(0, u) + user;
    }
    form = document.forms['login'];
    form.elements['openId'].value = openid;
}