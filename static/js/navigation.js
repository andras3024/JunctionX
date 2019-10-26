console.log('Navigation 2.0');

$('.select_card_button').click(select_card);
$('.generate_qr_button').click(generate_qr);

function select_card(){
  window.location.href = window.location.href + '_' +this.getAttribute('data-id')+'/stat'
}

function generate_qr(){
  console.log(window.location.href + '_' +this.getAttribute('data-id')+'/qr');
  window.location.href = window.location.href + '_' +this.getAttribute('data-id')+'/qr'
}
