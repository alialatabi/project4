function show_edit(id) {
    var edit_div = document.querySelector(`#edit_div_${id}`);
    var edit_box = document.querySelector(`#edit_box_${id}`);
    var content = document.querySelector(`#content_${id}`);


    content.style.display = 'none';
    edit_box.value = content.innerHTML
    edit_div.style.display = 'block';
}

function edit(id) {
    var edit_div = document.querySelector(`#edit_div_${id}`);
    var edit_box = document.querySelector(`#edit_box_${id}`);
    var content = document.querySelector(`#content_${id}`);

    fetch(`/edit/${id}`, {
        method: 'PUT',
        body: JSON.stringify({
            post: edit_box.value
        })
    });

    content.innerHTML = edit_box.value;
    edit_div.style.display = 'none';
    content.style.display = 'block';
    edit_box.value = "";
}

function like(id) {
    btn = document.querySelector(`#like_${id}`)
    counter = document.querySelector(`#like_count_${id}`)
    if (btn.value === '🤍') {
        fetch(`/like/${id}`, {
            method: 'POST',
            body: JSON.stringify({
                add: true
            })
        })

        btn.value = '❤'
    } else if (btn.value === '❤'){
        fetch(`/like/${id}`, {
            method: 'POST',
            body: JSON.stringify({
                add: false
            })
        })
        btn.value = '🤍'
    }

    fetch(`/like/${id}`)
        .then(response => response.json())
        .then(post => {
            counter.innerHTML = post.like_count + ' Likes';
        });

}