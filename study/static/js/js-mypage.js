// function loadContent(url) {
//             var xhr = new XMLHttpRequest();
//             xhr.open('GET', url, true);
//             xhr.onreadystatechange = function() {
//                 if (xhr.readyState == 4 && xhr.status == 200) {
//                     document.getElementById('content').innerHTML = xhr.responseText;
//                 }
//             };
//             xhr.send();
//         }

//         document.addEventListener('DOMContentLoaded', function() {
//             var radios = document.querySelectorAll('.dropdown-mypage input[type="radio"]');
//             radios.forEach(function(radio) {
//                 radio.addEventListener('change', function(event) {
//                     var url = event.target.value;
//                     loadContent(url);
//                 });
//             });
//         });

document.querySelectorAll('input[name="page"]').forEach(radio => {
    radio.addEventListener('change', function() {
        console.log('Radio button changed');
        document.getElementById('pageForm').submit();
    });
});
