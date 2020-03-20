function get()
{
    var list=document.getElementById("list");
    var item = document.createElement("li");
    var div = document.createElement("div");
    div.style.border="1px groove rgb(189, 199, 216)";
    div.style.borderRadius="2px";
    div.style.width="650px"
    div.style.padding="17px";
            
            
    var cbox=document.createElement("input");
    cbox.type= "checkbox";
                
                
    var label = document.createElement("label");
            
    label.innerText=document.getElementById("adder").value;
    label.style.position = "absolute";
    label.style.left="60px";
    label.id="lol";
                
    var del_but = document.createElement("input");
    del_but.type="image";
    del_but.style.width="18px";
    del_but.style.height="18px";
    del_but.src="https://cdn2.iconfinder.com/data/icons/e-business-helper/240/627249-delete3-512.png";
    del_but.style.position = "absolute";
    del_but.style.left="640px";
            
    div.appendChild(cbox);
    div.appendChild(label);
    div.appendChild(del_but);
    item.appendChild(div);
    list.appendChild(item);
            
            
    del_but.onclick=function f()
    {
        item.remove();
    }
            
    cbox.onclick=function t()
    {
        if(cbox.checked==true){
        label.style.textDecoration="line-through"}
        else label.style.textDecoration="";
    
    }
            
            
    document.getElementById("adder").value="";
            
    };
