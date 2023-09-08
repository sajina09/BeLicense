"use strict";(self.webpackChunkfelicense=self.webpackChunkfelicense||[]).push([[986],{9719:function(e,i,n){n.d(i,{Z:function(){return h}});var t=n(390),c=n(5242),l=n(4695),r=n(5080),s=n(5545),o=n(5400),d=n(891),a=n(9108),u=n(2559),h=function(e){var i=e.showAll,n=void 0!==i&&i,h=(0,d.T)(),x=(0,d.C)((function(e){return e.subjects})).fields,f=(0,s.s0)();(0,t.useEffect)((function(){h((0,a.O8)())}),[h]);var p=function(e){var i=e.replace(/\s+/g,"-");f("/".concat(i))};return(0,u.jsxs)("div",{className:"choose-course",children:[(0,u.jsxs)("div",{className:"section-course",children:[(0,u.jsx)(l.Z,{children:(0,u.jsx)(r.Z,{children:(0,u.jsxs)("h1",{className:"section-title-course",children:[" ","Choose your desired Program!"]})})}),(0,u.jsx)(l.Z,{children:(0,u.jsx)(r.Z,{children:(0,u.jsx)("p",{className:"section-content",children:"Please select one"})})}),(0,u.jsx)(c.ZP,{className:"see-more-btn",type:"link",children:(0,u.jsx)(o.rU,{to:"/all-fields",children:"See all courses"})})]}),(0,u.jsx)("div",{className:"fields-container",children:function(){var e=n?null===x||void 0===x?void 0:x.length:6;return(0,u.jsx)(u.Fragment,{children:null===x||void 0===x?void 0:x.slice(0,e).map((function(e,i){return(0,u.jsx)(c.ZP,{className:"field-btn",title:e.subject_name,onClick:function(){p(e.subject_name)},children:(0,u.jsx)("div",{style:{width:"100%",overflow:"hidden",textOverflow:"ellipsis",whiteSpace:"nowrap"},children:e.subject_name})},i)}))})}()})]})}},4359:function(e,i,n){n.d(i,{Z:function(){return s}});n(390);var t=n(1200),c=n(7406),l=n(2559),r=t.Z.Meta,s=function(e){var i=e.title,n=e.description,s=e.button,o=e.children;return(0,l.jsxs)(t.Z,{className:"ticket",bordered:!1,children:[(0,l.jsx)(r,{title:i}),(0,l.jsx)("div",{className:"ticket-description",children:n}),o,s&&(0,l.jsx)(c.Z,{children:s})]})}},891:function(e,i,n){n.d(i,{C:function(){return c},T:function(){return l}});var t=n(1750),c=t.v9,l=function(){return(0,t.I0)()}},7986:function(e,i,n){n.r(i),n.d(i,{default:function(){return w}});var t=n(9439),c=n(390),l=n(4695),r=n(5080),s=n(9753),o=n(4359),d=n(9719),a=n(2559),u={chapters:[{id:"1",title:"Chapter 1 : Concept of Basic ELectrical and Electronics Engineering",subtopics:[{id:"1",title:"1.1 Basic Concept",subtopics:["Second Subtopic","Second Sub Second Sub topic topic Second Subtopic Second Subtopic Second Subtopic"]},{id:"2",title:"1.2 Second Subtopic"},{id:"3",title:"1.3 Third Subtopic"},{id:"4",title:"1.4 Fourth Subtopic"},{id:"5",title:"1.5 Fifth Subtopic"},{id:"6",title:"1.6 Sixth Subtopic"}]}]},h=function(){return(0,a.jsx)("div",{children:u.chapters.map((function(e){return(0,a.jsxs)("div",{children:[(0,a.jsx)("h3",{children:e.title}),(0,a.jsx)(l.Z,{gutter:[16,16],wrap:!0,children:e.subtopics.map((function(e){var i;return(0,a.jsxs)(r.Z,{span:8,children:[(0,a.jsx)("div",{className:"chapter-name",children:e.title}),null===e||void 0===e||null===(i=e.subtopics)||void 0===i?void 0:i.map((function(e){return(0,a.jsx)("ul",{children:(0,a.jsx)("li",{children:e})})}))]},e.id)}))})]},e.id)}))})},x=n(4942),f=n(1413),p=n(1200),j=n(9040),v=n(1279),m=n(891),b=n(9108),g=function(){var e,i,n=(0,m.T)(),l=(0,m.C)((function(e){return e.subjects})).modelset;(0,c.useEffect)((function(){n((0,b.Gz)())}),[]);var r=(0,c.useState)({}),s=(0,t.Z)(r,2),o=s[0],d=s[1],u=null===l||void 0===l||null===(e=l[0])||void 0===e?void 0:e.questions,h=null===l||void 0===l||null===(i=l[0])||void 0===i?void 0:i.set_name;return(0,a.jsxs)("div",{children:[(0,a.jsx)("h1",{style:{textAlign:"center"},children:h}),null===u||void 0===u?void 0:u.map((function(e,i){var n=o[e.id],t=n===e.correct_answer;return(0,a.jsxs)(p.Z,{title:(0,a.jsx)("div",{dangerouslySetInnerHTML:{__html:'<div style="display: flex; align-items: center;">'.concat(i+1,". &nbsp;").concat(e.title,"</div>")}}),children:[(0,a.jsx)(j.ZP.Group,{style:{display:"flex",flexDirection:"column"},className:"vertical-radio-group",onChange:function(i){return n=e.id,t=i.target.value,void setTimeout((function(){d((function(e){return(0,f.Z)((0,f.Z)({},e),{},(0,x.Z)({},n,t))}))}),100);var n,t},children:["A","B","C","D"].map((function(i){return(0,a.jsx)(j.ZP,{value:i,style:{color:n&&i===n?t?"green":"red":"black"},children:(0,a.jsx)("p",{style:{borderRadius:"8px",lineHeight:"0px",padding:"1px 8px",backgroundColor:n&&i===n?t?"#daedd1":"#f5dada":"white"},dangerouslySetInnerHTML:{__html:e[i]}})},i)}))}),(0,a.jsx)(v.Z,{style:{marginTop:"10px"},items:[{key:"1",label:"Answer",children:(0,a.jsx)("div",{style:{borderRadius:"8px",backgroundColor:"rgb(255 245 231)",padding:"10px",margin:0},dangerouslySetInnerHTML:{__html:e.explanation}}),extra:(0,a.jsx)("div",{children:"Similar questions"})}]})]},e.id)}))]})},Z=n(2674),S=n(7406),y=[{title:"Title 1"},{title:"Title 2"},{title:"Title 3"},{title:"Title 4"}],C=function(){var e=function(){console.log("hi")},i=function(){};return(0,a.jsx)(Z.Z,{grid:{gutter:16,column:4},dataSource:y,renderItem:function(n){return(0,a.jsx)(Z.Z.Item,{children:(0,a.jsx)(p.Z,{title:n.title,children:(0,a.jsxs)("div",{style:{display:"flex",flexDirection:"row",justifyContent:"space-around"},children:[(0,a.jsx)(S.Z,{onClick:e,children:" Practice"}),(0,a.jsx)(S.Z,{onClick:i,children:" Take Exam"})]})})})}})},T=n(1069),k=[{id:"1",title:"Chapter 1",url:"https://example.com/course1"},{id:"2",title:"Chapter 2",url:"https://example.com/course2"}],w=function(){var e=(0,c.useState)(null),i=(0,t.Z)(e,2),n=i[0],u=i[1];return(0,a.jsxs)("div",{className:"course-specific-container",children:[(0,a.jsxs)(T.ql,{children:[(0,a.jsx)("title",{children:"Syllabus"}),(0,a.jsx)("meta",{name:"description",content:"Syllabus for nec engineering license of IT."}),(0,a.jsx)("link",{rel:"canonical",href:"/Information-Technology-&-Telecommunication-Engineering"})]}),(0,a.jsx)("div",{className:"course-specific-name",style:{width:"400px"},children:(0,a.jsx)(o.Z,{title:"Information Technology",description:"A detailed, reliable view of your IT knowledge in a quick convenient format."})}),(0,a.jsx)("div",{className:"section",children:(0,a.jsx)(l.Z,{children:(0,a.jsx)(r.Z,{children:(0,a.jsx)("h1",{className:"section-title",children:"Available Model Questions"})})})}),(0,a.jsx)(C,{}),(0,a.jsx)(g,{}),(0,a.jsx)(s.Z,{tabPosition:"top",defaultActiveKey:"0",className:"chapter-tab",onChange:function(e){var i=k.find((function(i){return i.id===e}));u(i||null)},children:k.map((function(e){return(0,a.jsx)(s.Z.TabPane,{tab:e.title,children:n&&(0,a.jsx)("div",{children:(0,a.jsx)(h,{})})},e.id)}))}),(0,a.jsx)(d.Z,{})]})}}}]);
//# sourceMappingURL=986.c4448844.chunk.js.map