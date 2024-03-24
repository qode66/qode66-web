(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[371],{4764:function(e,t,r){"use strict";r.d(t,{$:function(){return d}});var n=r(7294),a=r(3967),i=r.n(a);let c={size:{type:"enum",values:["1","2","3"],default:"3",responsive:!0},display:{type:"enum",values:["none","block"],default:void 0,responsive:!0}};var o=r(3843),l=r(134),s=r(6776);let d=n.forwardRef((e,t)=>{let{rest:r,...a}=(0,o.FY)(e),{rest:d,...f}=(0,l.F8)(r),{className:u,size:h=c.size.default,display:g=c.display.default,...p}=d;return n.createElement("section",{...p,ref:t,className:i()("rt-Section",u,(0,s.g)(h,"rt-r-size"),(0,s.g)(g,"rt-r-display"),(0,l.yt)(f),(0,o.we)(a))})});d.displayName="Section"},1641:function(e,t,r){(window.__NEXT_P=window.__NEXT_P||[]).push(["/portfolio",function(){return r(9457)}])},9457:function(e,t,r){"use strict";r.r(t),r.d(t,{Link_1d4257c600beccd47c19a285131f648a:function(){return Link_1d4257c600beccd47c19a285131f648a},Link_3eb9bbc9cb7930dce096d39126616862:function(){return Link_3eb9bbc9cb7930dce096d39126616862},Link_58ad130191d5d6032e4bbb0cc30d8ae6:function(){return Link_58ad130191d5d6032e4bbb0cc30d8ae6},Link_6283293296957734b380ee6bb4c3a58c:function(){return Link_6283293296957734b380ee6bb4c3a58c},Link_b1af009e93c88f8bd727398c7e8ea626:function(){return Link_b1af009e93c88f8bd727398c7e8ea626},Link_c4054b67aad36d54c3647e5517f7d3a3:function(){return Link_c4054b67aad36d54c3647e5517f7d3a3},default:function(){return Component}});var n=r(2364),a=r(7294),i=r(2627),c=r(5877),o=r(3967),l=r.n(o),s=r(7462),d=r(5360),f=r(9698),u=r(9981),h=r(5320);let g="Avatar",[p,m]=(0,d.b)(g),[b,x]=p(g),y=(0,a.forwardRef)((e,t)=>{let{__scopeAvatar:r,...n}=e,[i,c]=(0,a.useState)("idle");return(0,a.createElement)(b,{scope:r,imageLoadingStatus:i,onImageLoadingStatusChange:c},(0,a.createElement)(h.WV.span,(0,s.Z)({},n,{ref:t})))}),k=(0,a.forwardRef)((e,t)=>{let{__scopeAvatar:r,src:n,onLoadingStatusChange:i=()=>{},...c}=e,o=x("AvatarImage",r),l=$cddcb0b647441e34$var$useImageLoadingStatus(n),d=(0,f.W)(e=>{i(e),o.onImageLoadingStatusChange(e)});return(0,u.b)(()=>{"idle"!==l&&d(l)},[l,d]),"loaded"===l?(0,a.createElement)(h.WV.img,(0,s.Z)({},c,{ref:t,src:n})):null}),w=(0,a.forwardRef)((e,t)=>{let{__scopeAvatar:r,delayMs:n,...i}=e,c=x("AvatarFallback",r),[o,l]=(0,a.useState)(void 0===n);return(0,a.useEffect)(()=>{if(void 0!==n){let e=window.setTimeout(()=>l(!0),n);return()=>window.clearTimeout(e)}},[n]),o&&"loaded"!==c.imageLoadingStatus?(0,a.createElement)(h.WV.span,(0,s.Z)({},i,{ref:t})):null});function $cddcb0b647441e34$var$useImageLoadingStatus(e){let[t,r]=(0,a.useState)("idle");return(0,u.b)(()=>{if(!e){r("error");return}let t=!0,n=new window.Image,updateStatus=e=>()=>{t&&r(e)};return r("loading"),n.onload=updateStatus("loaded"),n.onerror=updateStatus("error"),n.src=e,()=>{t=!1}},[e]),t}var Z=r(8291),v=r(6679),_=r(269);let S={type:"enum",values:_.yT.radius.values,default:void 0},L={size:{type:"enum",values:["1","2","3","4","5","6","7","8","9"],default:"3",responsive:!0},variant:{type:"enum",values:["solid","soft"],default:"soft"},color:{...Z.m,default:void 0},highContrast:v.B,radius:S,fallback:{type:"ReactNode",default:void 0,required:!0}};var C=r(3843),W=r(6776);let X=a.forwardRef((e,t)=>{let{rest:r,...n}=(0,C.FY)(e),{className:i,style:c,size:o=L.size.default,variant:s=L.variant.default,color:d=L.color.default,highContrast:f=L.highContrast.default,radius:u=L.radius.default,fallback:h,...g}=r,[p,m]=a.useState("idle");return a.createElement(y,{"data-accent-color":d,"data-radius":u,className:l()("rt-AvatarRoot",i,(0,W.g)(o,"rt-r-size"),`rt-variant-${s}`,{"rt-high-contrast":f},(0,C.we)(n)),style:c},"idle"===p||"loading"===p?a.createElement("span",{className:"rt-AvatarFallback"}):null,"error"===p?a.createElement(w,{className:l()("rt-AvatarFallback",{"rt-one-letter":"string"==typeof h&&1===h.length,"rt-two-letters":"string"==typeof h&&2===h.length}),delayMs:0},h):null,a.createElement(k,{ref:t,className:"rt-AvatarImage",...g,onLoadingStatusChange:e=>{var t;null===(t=g.onLoadingStatusChange)||void 0===t||t.call(g,e),m(e)}}))});X.displayName="Avatar";var z=r(6445),F=r(1675),B=r(4764),A=r(1042),q=r(8426);let E={size:{type:"enum",values:["1","2","3","4","5"],default:"1",responsive:!0},variant:{type:"enum",values:["surface","classic","ghost"],default:"surface"}},M=a.forwardRef((e,t)=>{let{rest:r,...n}=(0,C.FY)(e),{asChild:i,children:c,className:o,size:s=E.size.default,variant:d=E.variant.default,...f}=r,u=i?q.g7:"div";function getChild(){let e=a.Children.only(c);return a.cloneElement(e,{children:a.createElement("div",{className:"rt-CardInner"},e.props.children)})}return a.createElement(u,{ref:t,...f,className:l()("rt-reset","rt-Card",o,(0,W.g)(s,"rt-r-size"),`rt-variant-${d}`,(0,C.we)(n))},i?getChild():a.createElement("div",{className:"rt-CardInner"},c))});M.displayName="Card";var R=r(1664),j=r.n(R),N=r(6608),H=r(9008),I=r.n(H);function Link_1d4257c600beccd47c19a285131f648a(){return(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://github.com/qode66/guia-markdown-ca",passHref:!0,children:(0,n.BX)(c.k,{align:"center",gap:"2",children:[(0,n.tZ)(X,{src:"/icons/github.png"}),(0,n.tZ)(z.x,{as:"p",css:{color:"black"},children:"Veure a GitHub"})]})})})}function Link_b1af009e93c88f8bd727398c7e8ea626(){return(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://mastodon.social/@qode66",passHref:!0,children:"Mastodon"})})}function Link_6283293296957734b380ee6bb4c3a58c(){return(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://www.linkedin.com/in/qserrano/",passHref:!0,children:"LinkedIn"})})}function Link_3eb9bbc9cb7930dce096d39126616862(){return(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://github.com/qode66",passHref:!0,children:"Github"})})}function Link_c4054b67aad36d54c3647e5517f7d3a3(){return(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://github.com/qode66/arduino-tutorial",passHref:!0,children:(0,n.BX)(c.k,{align:"center",gap:"2",children:[(0,n.tZ)(X,{src:"/icons/github.png"}),(0,n.tZ)(z.x,{as:"p",css:{color:"black"},children:"Veure a GitHub"})]})})})}function Link_58ad130191d5d6032e4bbb0cc30d8ae6(){return(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},target:(0,N.oA)(!0)?"_blank":"",children:(0,n.tZ)(j(),{href:"https://github.com/qode66/arduino-scratch",passHref:!0,children:(0,n.BX)(c.k,{align:"center",gap:"2",children:[(0,n.tZ)(X,{src:"/icons/github.png"}),(0,n.tZ)(z.x,{as:"p",css:{color:"black"},children:"Veure a GitHub"})]})})})}function Component(){return(0,n.BX)(a.Fragment,{children:[(0,n.BX)(F.W,{children:[(0,n.tZ)(F.W,{css:{position:"sticky",justify:"center",align:"center",width:"100%",height:"60px",background:"#1a1b1a",marginTop:"20px"},children:(0,n.BX)(c.k,{align:"start",direction:"row",gap:"2",children:[(0,n.BX)(c.k,{align:"start",direction:"row",gap:"2",children:[(0,n.tZ)("img",{css:{height:"30px",width:"auto"},src:"/images/quique-rounded.png"}),(0,n.tZ)(z.x,{as:"p",css:{color:"#3ece56",fontFamily:["Merryweather"],fontWeight:"500",fontStyle:"italic"},size:"5",weight:"regular",children:"Quique Serrano"})]}),(0,n.tZ)(c.k,{css:{flex:1,justifySelf:"stretch",alignSelf:"stretch"}}),(0,n.BX)(c.k,{align:"start",css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"14px",color:"#c5f2f3"},direction:"row",gap:"2",children:[(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"/",passHref:!0,children:"Inici"})}),(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"/portfolio",passHref:!0,children:"Portfoli"})}),(0,n.tZ)(i.r,{asChild:!0,css:{color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"/about",passHref:!0,children:"Quant a"})})]})]})}),(0,n.tZ)(F.W,{children:(0,n.BX)(B.$,{children:[(0,n.tZ)(c.k,{css:{display:"flex",alignItems:"center",justifyContent:"center"},children:(0,n.tZ)(A.X,{css:{color:"#3ece56",fontSize:"40px",marginBottom:"20px",fontFamily:["Merryweather"],fontWeight:"700"},children:"Portfoli"})}),(0,n.BX)(B.$,{children:[(0,n.tZ)(A.X,{css:{color:"#3ece56",fontSize:"32px",margin:"20px",fontFamily:["Merryweather"],fontWeight:"700"},children:"Traduccions"}),(0,n.tZ)(F.W,{css:{marginTop:"10px",marginBottom:"10px"},children:(0,n.BX)(c.k,{css:{background:"#000201"},direction:"row",children:[(0,n.BX)(c.k,{align:"center",css:{width:"50%"},direction:"column",justify:"center",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"32px",color:"#684a3b",padding:"20px"},children:"Tutorial Scratch for Arduino S4A"}),(0,n.tZ)(z.x,{as:"p",css:{fontFamily:"Raleway",fontWeight:"300",fontSize:"16px",color:"#c5f2f3",padding:"20px"},children:"Scratch for Arduino S4A \xe9s un entorn senzill i divertit per als alumnes mes joves, que els inicia en aqueix cam\xed i els introdueix a els conceptes inherents a la programaci\xf3 estructurada d'una manera que sembla un joc, per\xf2 amb moltes mes profunditat del que a primera vista es percep."}),(0,n.tZ)(M,{css:{background:"#c5f2f3","&:hover":{opacity:"0.5"}},children:(0,n.tZ)(Link_c4054b67aad36d54c3647e5517f7d3a3,{})})]}),(0,n.tZ)(c.k,{align:"center",css:{width:"50%",padding:"10px"},justify:"center",children:(0,n.tZ)("img",{css:{width:"300px",height:"auto"},src:"/images/arduino-scratch.png"})})]})}),(0,n.tZ)(F.W,{css:{marginTop:"10px",marginBottom:"10px"},children:(0,n.BX)(c.k,{css:{background:"#1a1b1a"},direction:"row",children:[(0,n.BX)(c.k,{align:"center",css:{width:"50%"},direction:"column",justify:"center",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"32px",color:"#684a3b",padding:"20px"},children:"Tutorial de Arduino"}),(0,n.tZ)(z.x,{as:"p",css:{fontFamily:"Raleway",fontWeight:"300",fontSize:"16px",color:"#c5f2f3",padding:"20px"},children:"Descobreix la pot\xe8ncia d’Arduino mentre explorem el seu hardware senzill, el seu programari f\xe0cil d’utilitzar i les inacabables possibilitats de projectes. Des de circuits b\xe0sics fins a rob\xf2tica avan\xe7ada, aquest tutorial et dotar\xe0 del coneixement i les habilitats per fer realitat les teves idees."}),(0,n.tZ)(M,{css:{background:"#c5f2f3","&:hover":{opacity:"0.5"}},children:(0,n.tZ)(Link_58ad130191d5d6032e4bbb0cc30d8ae6,{})})]}),(0,n.tZ)(c.k,{align:"center",css:{width:"50%",padding:"10px"},justify:"center",children:(0,n.tZ)("img",{css:{width:"300px",height:"auto"},src:"/images/arduino-sensors.png"})})]})}),(0,n.tZ)(F.W,{css:{marginTop:"10px",marginBottom:"10px"},children:(0,n.BX)(c.k,{css:{background:"#000201"},direction:"row",children:[(0,n.BX)(c.k,{align:"center",css:{width:"50%"},direction:"column",justify:"center",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"32px",color:"#684a3b",padding:"20px"},children:"Refer\xe8ncia de programaci\xf3 d'arduino"}),(0,n.tZ)(z.x,{as:"p",css:{fontFamily:"Raleway",fontWeight:"300",fontSize:"16px",color:"#c5f2f3",padding:"20px"},children:"Traducci\xf3 al catal\xe0/valenci\xe0 de arduino/reference-en, la documentaci\xf3 de refer\xe8ncia del llenguatge de la sintaxi d’Arduino."}),(0,n.tZ)(M,{css:{background:"#c5f2f3","&:hover":{opacity:"0.5"}},children:(0,n.tZ)(Link_c4054b67aad36d54c3647e5517f7d3a3,{})})]}),(0,n.tZ)(c.k,{align:"center",css:{width:"50%",padding:"10px"},justify:"center",children:(0,n.tZ)("img",{css:{width:"300px",height:"auto"},src:"/images/arduino-refprog.png"})})]})}),(0,n.tZ)(F.W,{css:{marginTop:"10px",marginBottom:"10px"},children:(0,n.BX)(c.k,{css:{background:"#1a1b1a"},direction:"row",children:[(0,n.BX)(c.k,{align:"center",css:{width:"50%"},direction:"column",justify:"center",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"32px",color:"#684a3b",padding:"20px"},children:"Guia Markdown"}),(0,n.tZ)(z.x,{as:"p",css:{fontFamily:"Raleway",fontWeight:"300",fontSize:"16px",color:"#c5f2f3",padding:"20px"},children:"Traducci\xf3 al catal\xe0/valenci\xe0 de Markdown Guide. La Guia Markdown \xe9s una guia de refer\xe8ncia lliure i de codi obert que explica com utilitzar Markdown, el llenguatge de marcatge senzill i f\xe0cil d'utilitzar que podeu utilitzar per formatar pr\xe0cticament qualsevol document."}),(0,n.tZ)(M,{css:{background:"#c5f2f3","&:hover":{opacity:"0.5"}},children:(0,n.tZ)(Link_1d4257c600beccd47c19a285131f648a,{})})]}),(0,n.tZ)(c.k,{align:"center",css:{width:"50%",padding:"10px"},justify:"center",children:(0,n.tZ)("img",{css:{width:"300px",height:"auto"},src:"/images/markdown.png"})})]})})]})]})}),(0,n.tZ)(F.W,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"14px",color:"#c5f2f3",backgroundColor:"#1a1b1a",width:"100%",height:"20vh"},children:(0,n.BX)(c.k,{align:"start",direction:"row",gap:"2",children:[(0,n.BX)(c.k,{css:{width:"10%",display:"flex",alignItems:"center",justifyContent:"center"},direction:"column",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"14px",color:"#c5f2f3"},children:"\xa9 2024-2030"}),(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"mailto:qode66@gmail.com",passHref:!0,children:"Qode66"})})]}),(0,n.BX)(c.k,{css:{width:"10%",display:"flex",alignItems:"center",justifyContent:"center"},direction:"column",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"14px",color:"#c5f2f3"},children:"Social"}),(0,n.tZ)(Link_b1af009e93c88f8bd727398c7e8ea626,{}),(0,n.tZ)(Link_3eb9bbc9cb7930dce096d39126616862,{}),(0,n.tZ)(Link_6283293296957734b380ee6bb4c3a58c,{})]}),(0,n.BX)(c.k,{css:{width:"10%",display:"flex",alignItems:"center",justifyContent:"center"},direction:"column",children:[(0,n.tZ)(A.X,{css:{fontFamily:["Merryweather"],fontWeight:"700",fontSize:"14px",color:"#c5f2f3"},children:"Legal"}),(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"#",passHref:!0,children:"Privacitat"})}),(0,n.tZ)(i.r,{asChild:!0,css:{fontFamily:"Raleway",fontWeight:"300",color:"#c5f2f3",textDecoration:"none","&:hover":{color:"#3ece56"}},children:(0,n.tZ)(j(),{href:"#",passHref:!0,children:"Galetes"})})]})]})})]}),(0,n.BX)(I(),{children:[(0,n.tZ)("title",{children:"Portfolio"}),(0,n.tZ)("meta",{content:"favicon.ico",property:"og:image"})]})]})}}},function(e){e.O(0,[538,774,888,179],function(){return e(e.s=1641)}),_N_E=e.O()}]);