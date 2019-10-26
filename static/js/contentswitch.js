console.log('Content Switch');
const next_content_url = JSON.parse(document.getElementById('next_content_url').textContent);
var vid = document.getElementById("myVideo");

// Functions on key down events (Enter,Right Arrow,Left Arrow)
document.onkeydown = function(event) {
    if (event.key === 'ArrowRight'){
        window.location.pathname = next_content_url;
    }
}

vid.onended = function() {
   window.location.pathname = next_content_url;
};