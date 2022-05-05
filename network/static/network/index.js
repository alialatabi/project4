function show_edit(id) {
    const edit_div = document.querySelector(`#edit_div_${id}`);
    const edit_box = document.querySelector(`#edit_box_${id}`);
    const content = document.querySelector(`#content_${id}`);


    content.style.display = 'none';
    edit_box.value = content.innerHTML
    edit_div.style.display = 'block';
}

function edit(id) {
    const edit_div = document.querySelector(`#edit_div_${id}`);
    const edit_box = document.querySelector(`#edit_box_${id}`);
    const content = document.querySelector(`#content_${id}`);

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
    let btn = document.querySelector(`#like_${id}`)
    let counter = document.querySelector(`#like_count_${id}`)
    fetch(`/like/${id}`, {
    }).then(response => response.json())
        .then(post => {
            counter.innerHTML = post.likes + ' Likes';
            btn.value = post.btn_val;
        });

}