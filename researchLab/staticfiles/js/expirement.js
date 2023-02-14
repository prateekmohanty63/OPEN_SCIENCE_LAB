var i=2;
    function addField(event)
    {
        event.preventDefault();
    
       var div=document.createElement('div')
       div.setAttribute('id','div'+i)

       // label for ingredient

       var label=document.createElement('label')
       label.setAttribute('for','ingredient'+i)
       label.innerHTML="Ingredient"
       div.appendChild(label)

       // making ingredient input

       var input=document.createElement('input')
       input.setAttribute('type','text')
       input.setAttribute('name','ingredient'+i)
       div.appendChild(input)

       var label1=document.createElement('label')
       label1.setAttribute('for','amt'+i)
       label1.innerHTML="Amount(g)"
       div.appendChild(label1)


       var amt=document.createElement('input')
       amt.setAttribute('type','text')
       amt.setAttribute('name','amt'+i)
       div.appendChild(amt)
      

    //    const node=document.getElementById('iform')
    //    const clone=node.cloneNode(true)

       document.getElementById('iform').appendChild(div)

       // label
       
       i++;

       document.getElementById('ninputs').value=i;

      
    }


    var dest='0';
   
    function click1(event)
    {
        event.preventDefault();
        dest+='1';

        let pickPlace=prompt("Press 1 for pickup or 2 for place: ")
        console.log(pickPlace)
      
        document.getElementById('slot').value=dest+","+pickPlace
        console.log("Inside js")

       
     
       // return false
    }
    function click2(event)
    {
        event.preventDefault();
        dest+='2';
        let pickPlace=prompt("Press 1 for pickup or 2 for place: ")
        console.log(pickPlace)
      
        document.getElementById('slot').value=dest+","+pickPlace
        // document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
        //return false
    }

    function click3(event)
    {
        event.preventDefault();
        dest+='3';
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
        //return false
    }
    function click4(event)
    {
        event.preventDefault();
        dest+='4';
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
        //return false
    }
    function click5(event)
    {
        event.preventDefault();
        dest+='5';
        console.log(dest)
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
        //return false
    }
  
    function click6(event)
    {
        event.preventDefault();
        dest+='6';
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
      //   console.log(dest)
      //return false
    }
  
    function click7(event)
    {
        event.preventDefault();
        dest+='7';
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
     //   console.log(dest)
       //return false
    }
  
    function click8(event)
    {
        event.preventDefault();
        dest+='8';
        console.log(dest)
        document.getElementById('slot').value=dest

        document.getElementById('expText').innerHTML+='ZN+HCL -> ZNCL2+H2'
        //return false
    }
  
