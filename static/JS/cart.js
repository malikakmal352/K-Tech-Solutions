
var updatesBtn  = document.getElementsByClassName('update-cart')

for (i=0; i < updatesBtn.length; i++) {
  updatesBtn[i].addEventListener('click' , function(){
    var productId = this.dataset.product
    var action = this.dataset.action
    console.log('productId:', productId , 'action:', action)
  })
}