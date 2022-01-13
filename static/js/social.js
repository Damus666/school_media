function commentReplyToggle(parent_id) {
    const row = document.getElementById(parent_id);
    if(row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

function shareToggle(parent_id) {
    const row = document.getElementById(parent_id);
    if(row.classList.contains('d-none')){
        row.classList.remove('d-none');
    } else {
        row.classList.add('d-none');
    }
}

function show(){
    const container = document.getElementById('notification-container');
    if (container.classList.contains('d-none')) {
        container.classList.remove('d-none')
    } else {
        container.classList.add('d-none')
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function remove(removeNotificationURL,redirectURL){
    const csrftoken = getCookie('csrftoken');
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
            if (xmlhttp.status == 200) {
                window.location.replace(redirectURL);
            } else {
                alert('There Was an Error');
            }
        }
    };

    xmlhttp.open("DELETE",removeNotificationURL, true);
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlhttp.send();
}

function formatTags() {
    const elements = document.getElementsByClassName('body');
    for (let i = 0; i < elements.length; i++) {
        let bodyText = elements[i].children[0].innerText;

        let words = bodyText.split(' ');

        for (let j = 0; j < words.length; j++) {
            if (words[j][0] === "#") {
                let replacedText = bodyText.replace(/\s\#(.*?)(\s|$)/g, `<a href="/social/explore/tags?query=${words[j].substring(1)}" class="post-link"> ${words[j]}</a>`)
                elements[i].innerHTML = replacedText
            }
        }
    }
}

formatTags();