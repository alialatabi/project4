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
    user = document.querySelector(`#like_${id}`).dataset.user
    console.log('like ' + user)
    // fetch('/like/' + parseInt(post), {
    //             method: 'POST',
    //             body: JSON.stringify({
    //                 post: post,
    //                 user: user,
    //             })
    //         }).then(r => 'liked')
}

// function like(event) {
//     document.querySelectorAll('[id^="like_"]').forEach(a => {
//         a.onclick = function () {
//             let post = this.dataset.id;
//             let user = this.dataset.user;
//             if (this.value === '🤍') {
//                 this.value = '❤'
//             } else {
//                 this.value = '🤍'
//             }
//             fetch('/like/' + parseInt(post), {
//                 method: 'POST',
//                 body: JSON.stringify({
//                     post: post,
//                     user: user,
//                 })
//             }).then(r => 'liked')
//         }
//
//     })
//
// }