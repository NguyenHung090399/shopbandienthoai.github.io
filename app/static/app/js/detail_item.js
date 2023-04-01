var updateBtns = document.getElementsByClassName('detail-item')
for(i = 0 ; i<updateBtns.length ; i++){
    updateBtns[i].addEventListener('click' , function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId , 'action:',action)
        console.log('User : ' , user)

        if(user === "AnonymousUser"){
            console.log("user not login")
        }else{
            updateUserOrder(productId , action)
        }
    })
}

function updateUserOrder(productId , action){
    console.log("user login")
    var url = '/detail_item/'
    fetch(url , {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json', 
            'X-CSRFToken': csrftoken
        },
        body : JSON.stringify({'productId':productId, 'action':action}) 
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log('Data', data)
        location.reload()
    })

}