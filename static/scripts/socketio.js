document.addEventListner('DOMContentLoader',()=>{
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    socket.on('connect',()={
        socket.send('I am connected');
    });
    // socket.on('message',()=>{
    //     const p=document.createElement('p');
    //     const br=document.createElement('br');
    //     p.innerHTML=data;
    //     document.querySelector('#').append(p)
    // });
    // #sending message
    // document.querySelector('#').onclick()=>{
    //     socket.send(document.querySelector('#').value)
    // }
    socket.on('message',data=>{
        console.log(data)
    });
})
