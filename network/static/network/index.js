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