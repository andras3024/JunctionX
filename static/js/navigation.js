console.log('Navigation 2.0');

$('.select_child_button').click(select_child);
$('.select_tale_button').click(select_tale);
$('.generate_qr_button').click(generate_qr);
$('.take_picture').click(take_picture);

function select_child(){
  window.location.href = window.location.href + 'child_' +this.getAttribute('data-id')+'/result'
}

function take_picture(){
  window.location.href = window.location.href + '/upload'
}

function select_tale(){
  window.location.href = window.location.href + '_' +this.getAttribute('data-id')+'/start'
}

function generate_qr(){
  console.log(window.location.href + 'child_' +this.getAttribute('data-id')+'/qr');
  window.location.href = window.location.href + 'child_' +this.getAttribute('data-id')+'/qr'
}
