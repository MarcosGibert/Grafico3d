<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Incidencias S4100 3D · P4</title><script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
html,body{margin:0;min-height:100%;font-family:Segoe UI,Helvetica,Arial,sans-serif;color:#2a3f5f;background:#fff}
.page{min-height:100vh;display:flex;flex-direction:column}
.toolbar{box-sizing:border-box;padding:6px 10px;border-bottom:1px solid #ddd;background:#f7f7f9;display:grid;grid-template-columns:minmax(260px,1fr) minmax(320px,1.3fr) 270px;gap:8px;align-items:start;max-height:200px;overflow:auto}
.panel,.toggles{background:white;border:1px solid #ddd;border-radius:7px;padding:5px 7px}
.title{font-weight:600;margin-bottom:4px;font-size:12px}
.checks{display:flex;flex-wrap:wrap;gap:3px 8px;max-height:48px;overflow:auto;font-size:10.5px;line-height:1.15}
.sub-search{width:100%;box-sizing:border-box;border:1px solid #c9cad1;border-radius:5px;padding:3px 6px;font-size:10.5px;color:#2a3f5f;margin-bottom:4px}
#subChecks,#elemChecks,#orgChecks{display:block;max-height:170px;overflow:auto;font-size:10.5px;line-height:1.3}
#subChecks .sub-standalone,#elemChecks .sub-standalone,#orgChecks .sub-standalone{display:block;padding:1px 0}
#subChecks .sub-group,#elemChecks .sub-group,#orgChecks .sub-group{margin:0}
#subChecks .sub-group>summary,#elemChecks .sub-group>summary,#orgChecks .sub-group>summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:4px;padding:1px 0}
#subChecks .sub-group>summary::-webkit-details-marker,#elemChecks .sub-group>summary::-webkit-details-marker,#orgChecks .sub-group>summary::-webkit-details-marker{display:none}
#subChecks .sub-group>summary::before,#elemChecks .sub-group>summary::before,#orgChecks .sub-group>summary::before{content:'▸';font-size:9px;color:#8a93a6;width:8px;display:inline-block;transition:transform .15s}
#subChecks .sub-group[open]>summary::before,#elemChecks .sub-group[open]>summary::before,#orgChecks .sub-group[open]>summary::before{transform:rotate(90deg)}
#subChecks .grp-label,#elemChecks .grp-label,#orgChecks .grp-label{display:flex;align-items:center;gap:3px;cursor:pointer}
#subChecks .grp-count,#elemChecks .grp-count,#orgChecks .grp-count{color:#8a93a6;font-size:9.5px;margin-left:2px}
#subChecks .sub-children,#elemChecks .sub-children,#orgChecks .sub-children{margin-left:15px;border-left:1px solid #e6e6ea;padding-left:6px}
#subChecks .sub-leaf,#elemChecks .sub-leaf,#orgChecks .sub-leaf{display:block;padding:1px 0}
label{white-space:nowrap}
.actions{display:flex;gap:5px;flex-wrap:wrap;margin-top:4px}
button{border:1px solid #c9cad1;background:white;color:#2a3f5f;border-radius:5px;padding:3px 6px;cursor:pointer;font-size:10.5px}
button:disabled{opacity:.38;cursor:not-allowed}
.primary{background:#2a3f5f;color:white}
.toggles{font-size:10.5px;min-width:245px}
.toggle-row{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-bottom:4px}
.p4-dot{display:inline-block;width:10px;height:10px;border-radius:2px;background:#E84620;margin-right:3px;vertical-align:middle}
.color-by-label{font-weight:600;color:#5a6478}
.date-row{display:grid;grid-template-columns:auto 1fr;gap:4px 6px;align-items:center;margin-top:4px}
select{border:1px solid #c9cad1;border-radius:5px;padding:2px 5px;color:#2a3f5f;background:white;font-size:10.5px;min-width:0}
#status{margin-top:4px;font-size:10.5px;color:#5a6478;line-height:1.15}
#hint{margin-top:2px;font-size:10px;color:#8a93a6}
#chart{width:100%;height:calc(100vh - 120px);min-height:680px}
.js-plotly-plot .legend .scrollbar{display:block!important}
@media(max-width:1050px){.toolbar{grid-template-columns:1fr;max-height:320px}.checks{max-height:62px}#subChecks,#elemChecks,#orgChecks{max-height:140px}#chart{height:820px;min-height:820px}}
</style></head><body><div class="page"><div class="toolbar">
<div class="panel"><div class="title">Unidades</div><div id="unitChecks" class="checks"></div><div class="actions"><button id="unitsAll">Todas</button><button id="unitsNone">Ninguna</button></div></div>
<div class="panel"><div class="title" id="filterTitle">Subsistemas</div>
<div id="filterSub"><input type="text" id="subSearch" class="sub-search" placeholder="Buscar subsistema..." autocomplete="off"><div id="subChecks" class="checks"></div><div class="actions"><button id="subsAll">Todos</button><button id="subsNone">Ninguno</button></div></div>
<div id="filterElem" style="display:none"><input type="text" id="elemSearch" class="sub-search" placeholder="Buscar elemento..." autocomplete="off"><div id="elemChecks" class="checks"></div><div class="actions"><button id="elemAll">Todos</button><button id="elemNone">Ninguno</button></div></div>
<div id="filterOrg" style="display:none"><input type="text" id="orgSearch" class="sub-search" placeholder="Buscar órgano..." autocomplete="off"><div id="orgChecks" class="checks"></div><div class="actions"><button id="orgAll">Todos</button><button id="orgNone">Ninguno</button></div></div>
</div>
<div class="toggles">
  <div class="toggle-row">
    <label><input type="checkbox" id="showTotal"> Total por mes (todas unidades)</label>
    <label><input type="checkbox" id="showTotalUnidad"> Total por unidad (todos meses)</label>
    <label><input type="checkbox" id="autoApply" checked> Auto</label>
    <label><span class="p4-dot"></span><input type="checkbox" id="showP4" checked> Remates P4</label>
  </div>
  <div class="toggle-row">
    <span class="color-by-label">Colorear por:</span>
    <label><input type="radio" name="colorBy" value="subsistema" checked> Subsistema</label>
    <label><input type="radio" name="colorBy" value="elemento"> Elemento</label>
    <label><input type="radio" name="colorBy" value="organo"> Órgano</label>
  </div>
  <div class="date-row"><span>Mes inicio</span><select id="startMonth"></select><span>Mes fin</span><select id="endMonth"></select></div>
  <div class="actions"><button id="apply" class="primary">Aplicar filtros</button><button id="btnUndo" disabled>↩ Deshacer</button></div>
  <div id="status"></div>
  <div id="hint">💡 Clic en un bloque para aislar su subsistema (botón "Todos" en Subsistemas para deshacerlo)</div>
</div>
</div><div id="chart"></div></div>
<script>
(function(){'use strict';
const P=__PAYLOAD__;
const rows=P.rows,unidades=P.unidades,meses=P.meses,subsistemas=P.subsistemas,elementos=P.elementos,organos=P.organos;
const colorMapSub=P.colorMapSub,colorMapElem=P.colorMapElem,colorMapOrg=P.colorMapOrg;
const subsColorSet=new Set(P.subsColor||[]),elemColorSet=new Set(P.elemColor||[]),orgColorSet=new Set(P.orgColor||[]);
const HW=P.hw,GAP=P.gap,GAP_TOTAL=P.gapTotal,TOTAL=P.etiquetaTotal,ORDEN=P.ordenApilado,UMBRAL=P.umbral,P4C=P.p4Color;
const gd=document.getElementById('chart'),status=document.getElementById('status');
const ci=[0,0,4,4,0,0,1,1,2,2,3,3],cj=[1,2,5,6,1,5,2,6,3,7,0,4],ck=[2,3,6,7,5,4,6,5,7,6,4,7];
let saved=null,recovering=false,clickBound=false,colorBy='subsistema';
const MAX_UNDO=20;
let undoStack=[],lastRenderedState=null;
// Para agrupar el árbol de Elementos bajo su Órgano real (no un heurístico).
const elemToOrg={};
for(const r of rows){elemToOrg[r.Elemento]=r.Organo;}
const NIVEL={subsistema:{titulo:'Subsistemas',corto:'subsist.',singular:'subsistema'},elemento:{titulo:'Elementos',corto:'elem.',singular:'elemento'},organo:{titulo:'Órganos',corto:'órg.',singular:'órgano'}};


function esc(s){return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
function norm(s){return String(s).normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();}
function checks(id,items,prefix){document.getElementById(id).innerHTML=items.map((x,i)=>`<label><input type="checkbox" id="${prefix}${i}" value="${esc(x)}" checked> ${esc(x)}</label>`).join('');}
function options(id,items,selectedIdx){document.getElementById(id).innerHTML=items.map((x,i)=>`<option value="${i}" ${i===selectedIdx?'selected':''}>${esc(x)}</option>`).join('');}

// ── Árbol jerárquico reutilizable para los 3 niveles: agrupa cada entrada bajo
// su padre (parent===value ⇒ entrada "suelta"/general de ese grupo), con
// buscador y checkboxes tri-estado en el grupo, al estilo del filtro de Excel.
function buildGroupedTree(entries,prefix){
  const groups=new Map();
  for(const e of entries){
    if(e.parent===e.value){
      if(!groups.has(e.value))groups.set(e.value,{self:null,children:[]});
      groups.get(e.value).self=e.value;
    }else{
      if(!groups.has(e.parent))groups.set(e.parent,{self:null,children:[]});
      groups.get(e.parent).children.push({full:e.value,label:e.label});
    }
  }
  const parents=Array.from(groups.keys()).sort((a,b)=>a.localeCompare(b,'es'));
  let n=0,html='';
  for(const p of parents){
    const g=groups.get(p);
    if(g.children.length===0){
      html+=`<label class="sub-standalone" data-search="${esc(norm(p))}"><input type="checkbox" id="${prefix}${n++}" value="${esc(p)}" checked> ${esc(p)}</label>`;
      continue;
    }
    g.children.sort((a,b)=>a.label.localeCompare(b.label,'es'));
    const items2=g.self?[{full:g.self,label:'(general)'},...g.children]:g.children;
    const total=items2.length;
    const childHtml=items2.map(it=>`<label class="sub-leaf" data-search="${esc(norm(it.full))}"><input type="checkbox" id="${prefix}${n++}" value="${esc(it.full)}" checked> ${esc(it.label)}</label>`).join('');
    html+=`<details class="sub-group" data-search="${esc(norm(p))}"><summary><label class="grp-label" onclick="event.stopPropagation()"><input type="checkbox" class="grp-toggle" checked> <b>${esc(p)}</b></label><span class="grp-count">(${total})</span></summary><div class="sub-children">${childHtml}</div></details>`;
  }
  return html;
}
// Listas de entradas por nivel: Subsistema se agrupa por el patrón "Sistema -
// Componente" (heurístico de texto); Elemento se agrupa por su Órgano real
// (dato de la jerarquía); Órgano no tiene padre, queda como lista plana.
function subEntries(items){
  return items.map(s=>{
    const idx=s.indexOf(' - ');
    if(idx>-1)return {value:s,parent:s.slice(0,idx).trim(),label:s.slice(idx+3).trim()};
    return {value:s,parent:s,label:s};
  });
}
function elemEntries(items){
  return items.map(e=>{
    const org=elemToOrg[e]||e;
    return org===e?{value:e,parent:e,label:e}:{value:e,parent:org,label:e};
  });
}
function orgEntries(items){return items.map(o=>({value:o,parent:o,label:o}));}
function syncGroupToggle(grp){
  const toggle=grp.querySelector('.grp-toggle'),kids=grp.querySelectorAll('.sub-leaf input[type=checkbox]');
  const n=kids.length,c=Array.from(kids).filter(k=>k.checked).length;
  toggle.checked=c===n;toggle.indeterminate=c>0&&c<n;
}
function isFilteredVisible(input){
  const leaf=input.closest('.sub-leaf,.sub-standalone');
  if(!leaf)return true;
  if(leaf.style.display==='none')return false;
  const grp=leaf.closest('.sub-group');
  return !(grp&&grp.style.display==='none');
}
function filterTree(rootId,q){
  const q2=norm(q.trim()),root=document.getElementById(rootId);
  root.querySelectorAll('.sub-group').forEach(g=>{
    if(!q2){g.style.display='';g.querySelectorAll('.sub-leaf').forEach(l=>l.style.display='');return;}
    const groupMatches=g.dataset.search.includes(q2);
    let any=false;
    g.querySelectorAll('.sub-leaf').forEach(leaf=>{
      const m=groupMatches||leaf.dataset.search.includes(q2);
      leaf.style.display=m?'':'none';
      if(m)any=true;
    });
    g.style.display=(groupMatches||any)?'':'none';
    if(any)g.open=true;
  });
  root.querySelectorAll('.sub-standalone').forEach(s=>{s.style.display=(!q2||s.dataset.search.includes(q2))?'':'none';});
}
function wireTree(id){
  document.getElementById(id).addEventListener('change',e=>{
    const t=e.target;
    if(!(t instanceof HTMLInputElement)||t.type!=='checkbox')return;
    if(t.classList.contains('grp-toggle')){
      const grp=t.closest('.sub-group');
      grp.querySelectorAll('.sub-leaf input[type=checkbox]').forEach(c=>c.checked=t.checked);
    }else{
      const grp=t.closest('.sub-group');
      if(grp)syncGroupToggle(grp);
    }
    maybe();
  });
}
document.getElementById('subChecks').innerHTML=buildGroupedTree(subEntries(subsistemas),'s_');
document.getElementById('elemChecks').innerHTML=buildGroupedTree(elemEntries(elementos),'e_');
document.getElementById('orgChecks').innerHTML=buildGroupedTree(orgEntries(organos),'o_');
wireTree('subChecks');wireTree('elemChecks');wireTree('orgChecks');
document.getElementById('subSearch').addEventListener('input',e=>filterTree('subChecks',e.target.value));
document.getElementById('elemSearch').addEventListener('input',e=>filterTree('elemChecks',e.target.value));
document.getElementById('orgSearch').addEventListener('input',e=>filterTree('orgChecks',e.target.value));
function updateActivePanel(){
  document.getElementById('filterSub').style.display=colorBy==='subsistema'?'':'none';
  document.getElementById('filterElem').style.display=colorBy==='elemento'?'':'none';
  document.getElementById('filterOrg').style.display=colorBy==='organo'?'':'none';
  document.getElementById('filterTitle').textContent=NIVEL[colorBy].titulo;
  document.getElementById('hint').textContent='💡 Clic en un bloque para aislar su '+NIVEL[colorBy].singular+' (botón "Todos" del panel para deshacerlo)';
}
checks('unitChecks',unidades,'u_');options('startMonth',meses,0);options('endMonth',meses,meses.length-1);
function selected(id){return Array.from(document.querySelectorAll('#'+id+' input:checked:not(.grp-toggle)')).map(x=>x.value);}
function selectedMonths(){let a=+document.getElementById('startMonth').value,b=+document.getElementById('endMonth').value;if(a>b){const t=a;a=b;b=t;}return meses.slice(a,b+1);}
function setAll(id,val){
  document.querySelectorAll('#'+id+' input[type=checkbox]').forEach(x=>{
    if(x.classList.contains('grp-toggle'))return;
    if(isFilteredVisible(x))x.checked=val;
  });
  document.querySelectorAll('#'+id+' .sub-group').forEach(syncGroupToggle);
  maybe();
}
function maybe(){if(document.getElementById('autoApply').checked)update();}
function colorFor(row){
  if(colorBy==='organo')return colorMapOrg[row.Organo]||'#C7C2BE';
  if(colorBy==='elemento')return colorMapElem[row.Elemento]||'#C7C2BE';
  return colorMapSub[row.Subsistema]||'#C7C2BE';
}
function r2(x){return Math.round(x*100)/100;}

// ── Añade un paralelepípedo a los arrays de mesh3d ───────────────────────────
function pushBox(X,Y,Z,I,J,K,FC,x0,y0,z0,z1,clr){
  let n0=X.length;
  X.push(x0-HW,x0+HW,x0+HW,x0-HW,x0-HW,x0+HW,x0+HW,x0-HW);
  Y.push(y0-HW,y0-HW,y0+HW,y0+HW,y0-HW,y0-HW,y0+HW,y0+HW);
  Z.push(z0,z0,z0,z0,z1,z1,z1,z1);
  I.push(...ci.map(a=>n0+a));J.push(...cj.map(a=>n0+a));K.push(...ck.map(a=>n0+a));
  for(let c=0;c<12;c++)FC.push(clr);
}

// Reparte varios puntos invisibles de hover por las caras visibles del bloque
// (laterales en x/y + arriba/abajo) en vez de un único punto enterrado en el
// centro del sólido, que solo queda "visible" para el picking según el ángulo
// de cámara. Así el hover responde de forma consistente mires desde donde mires.
function addHoverPoints(HX,HY,HZ,HT,HCD,x0,y0,z0,z1,txt,sub){
  const segH=z1-z0;
  const inset=HW*0.85;
  const diag=inset*0.7071;
  const ring=[[-inset,0],[inset,0],[0,-inset],[0,inset],[-diag,-diag],[diag,-diag],[-diag,diag],[diag,diag]];
  const nz=Math.max(1,Math.min(4,Math.round(segH*1.4)));
  for(let i=0;i<nz;i++){
    const z=r2(z0+segH*(i+0.5)/nz);
    for(const [dx,dy] of ring){HX.push(x0+dx);HY.push(y0+dy);HZ.push(z);HT.push(txt);HCD.push(sub);}
  }
  // Rejilla extra en la cara superior: casi siempre visible gracias al hueco
  // (GAP) que separa cada bloque del siguiente apilado encima.
  const topZ=r2(z1-segH*0.08),botZ=r2(z0+segH*0.08);
  const faceGrid=[[0,0],[-inset,0],[inset,0],[0,-inset],[0,inset]];
  for(const [dx,dy] of faceGrid){HX.push(x0+dx);HY.push(y0+dy);HZ.push(topZ);HT.push(txt);HCD.push(sub);}
  HX.push(x0);HY.push(y0);HZ.push(botZ);HT.push(txt);HCD.push(sub);
}

function build(selU,selF,selM,showTotalU,showP4,showTotalM,mode){
  const fieldName=mode==='organo'?'Organo':mode==='elemento'?'Elemento':'Subsistema';
  const us=new Set(selU),fs=new Set(selF),ms=new Set(selM);
  let f=rows.filter(r=>us.has(r.Unidad)&&fs.has(r[fieldName])&&ms.has(r.Mes));
  let draw=selU.slice();
  if(showTotalU){
    let acc=new Map();
    for(const r of f){let k=r.Mes+'||'+r.Subsistema;const o=acc.get(k)||{v:0,p4:0,organo:r.Organo,elemento:r.Elemento};o.v+=r.Valor;o.p4+=r.P4;acc.set(k,o);}
    for(const [k,o] of acc){let p=k.split('||');f.push({Unidad:TOTAL,Mes:p[0],Subsistema:p[1],Organo:o.organo,Elemento:o.elemento,Valor:o.v,P4:o.p4});}
    draw.push(TOTAL);
  }
  let drawM=selM.slice();
  if(showTotalM){
    let acc2=new Map();
    for(const r of f){
      if(r.Unidad===TOTAL)continue; // evitar la barra TOTAL×TOTAL
      let k=r.Unidad+'||'+r.Subsistema;const o=acc2.get(k)||{v:0,p4:0,organo:r.Organo,elemento:r.Elemento};o.v+=r.Valor;o.p4+=r.P4;acc2.set(k,o);
    }
    for(const [k,o] of acc2){let p=k.split('||');f.push({Unidad:p[0],Mes:TOTAL,Subsistema:p[1],Organo:o.organo,Elemento:o.elemento,Valor:o.v,P4:o.p4});}
    drawM.push(TOTAL);
  }
  const uIdx={};selU.forEach((u,i)=>uIdx[u]=i);if(showTotalU)uIdx[TOTAL]=selU.length+GAP_TOTAL;
  const mIdx={};selM.forEach((m,i)=>mIdx[m]=i);if(showTotalM)mIdx[TOTAL]=selM.length+GAP_TOTAL;
  const traces=[];let vertices=0;

  for(const u of draw){
    const X=[],Y=[],Z=[],I=[],J=[],K=[],FC=[],HX=[],HY=[],HZ=[],HT=[],HCD=[];
    for(const m of drawM){
      let g=f.filter(r=>r.Unidad===u&&r.Mes===m&&r.Valor>0);
      // Criterio de ordenación: cuando el modo es Órgano o Elemento, calculamos
      // primero el total de incidencias del grupo (todos los subsistemas del mismo
      // Órgano/Elemento en esta barra) y lo usamos como clave primaria. Así los
      // bloques del mismo grupo quedan juntos Y ordenados por el peso del grupo.
      // En modo Subsistema el comportamiento es el de siempre (por valor individual).
      if(mode!=='subsistema'){
        const grpField=mode==='organo'?'Organo':'Elemento';
        const grpTot=new Map();
        for(const r of g){grpTot.set(r[grpField],(grpTot.get(r[grpField])||0)+r.Valor);}
        g.sort((a,b)=>{
          const ta=grpTot.get(a[grpField]),tb=grpTot.get(b[grpField]);
          return ORDEN==='asc'
            ?ta-tb||a[grpField].localeCompare(b[grpField],'es')||a.Valor-b.Valor||a.Subsistema.localeCompare(b.Subsistema,'es')
            :tb-ta||a[grpField].localeCompare(b[grpField],'es')||b.Valor-a.Valor||a.Subsistema.localeCompare(b.Subsistema,'es');
        });
      }else{
        g.sort((a,b)=>ORDEN==='asc'?a.Valor-b.Valor||a.Subsistema.localeCompare(b.Subsistema):b.Valor-a.Valor||a.Subsistema.localeCompare(b.Subsistema));
      }
      let zb=0,x0=uIdx[u],y0=mIdx[m];
      for(const row of g){
        let v=+row.Valor, p4=showP4?Math.min(+row.P4||0,v):0;
        let z0=r2(zb), z1=r2(zb+v-(v>GAP*2?GAP:GAP*.5));
        let segH=z1-z0;

        if(p4>0 && p4<v){
          // Segmento inferior: incidencias no-P4 (color normal)
          let zSplit=r2(z0+(v-p4)/v*segH);
          pushBox(X,Y,Z,I,J,K,FC,x0,y0,z0,zSplit,colorFor(row));
          // Remate superior: incidencias P4 (naranja-rojo)
          pushBox(X,Y,Z,I,J,K,FC,x0,y0,zSplit,z1,P4C);
        } else if(p4>=v){
          // Todo P4
          pushBox(X,Y,Z,I,J,K,FC,x0,y0,z0,z1,P4C);
        } else {
          // Sin P4
          pushBox(X,Y,Z,I,J,K,FC,x0,y0,z0,z1,colorFor(row));
        }

        // Hover: mostrar ruta completa Órgano > Elemento > Subsistema + total + P4 si hay
        let p4txt=row.P4>0?`<br><span style="color:${P4C}">▲ P4 (reincidencia): <b>${row.P4}</b></span>`:'';
        let ruta=row.Organo?`<span style="color:#8a93a6;font-size:10px">${esc(row.Organo)} › ${esc(row.Elemento)}</span><br>`:'';
        let txt=`<b>${esc(u)}</b> · ${esc(m)}<br>${ruta}${esc(row.Subsistema)}: <b>${Math.round(v)}</b>${p4txt}`;
        let clickVal=mode==='organo'?row.Organo:mode==='elemento'?row.Elemento:row.Subsistema;
        addHoverPoints(HX,HY,HZ,HT,HCD,x0,y0,z0,z1,txt,clickVal);
        zb+=v;
      }
    }
    if(X.length){
      vertices+=X.length;
      traces.push({type:'mesh3d',x:X,y:Y,z:Z,i:I,j:J,k:K,facecolor:FC,hoverinfo:'skip',opacity:1,flatshading:true,lighting:{ambient:.55,diffuse:.7,specular:.08,roughness:.9,fresnel:.05},lightposition:{x:200,y:-300,z:400},showlegend:false,name:'Unidad '+u});
      traces.push({type:'scatter3d',x:HX,y:HY,z:HZ,mode:'markers',marker:{size:16,color:'rgba(0,0,0,0)'},hovertext:HT,customdata:HCD,hoverinfo:'text',hoverlabel:{bgcolor:'white',bordercolor:'#2a3f5f',font:{size:12,color:'#2a3f5f'}},showlegend:false,name:''});
    }
  }

  // Leyenda: categorías del nivel activo con suficientes incidencias, dentro
  // de lo seleccionado en el panel de filtros (que ahora coincide con el nivel).
  const sigSet=mode==='organo'?orgColorSet:mode==='elemento'?elemColorSet:subsColorSet;
  const cmap=mode==='organo'?colorMapOrg:mode==='elemento'?colorMapElem:colorMapSub;
  for(const val of selF){
    if(sigSet.has(val)){
      traces.push({type:'scatter3d',x:[null],y:[null],z:[null],mode:'markers',marker:{size:7,color:cmap[val],symbol:'square'},name:val,showlegend:true,hoverinfo:'skip'});
    }
  }
  // Leyenda: entrada P4 (solo si el toggle está activo)
  if(showP4){
    traces.push({type:'scatter3d',x:[null],y:[null],z:[null],mode:'markers',marker:{size:7,color:P4C,symbol:'square'},name:'▲ P4 – Reincidencia mantenimiento',showlegend:true,hoverinfo:'skip'});
  }

  return {traces,tickVals:draw.map(u=>uIdx[u]),tickText:draw.map(String),monthVals:drawM.map(m=>mIdx[m]),monthText:drawM,vertices};
}

function layout(vals,text,mVals,mText,showP4){
  let nivelTxt={subsistema:'Subsistemas',elemento:'Elementos',organo:'Órganos'}[colorBy];
  let sub='WebGL · multifiltro por unidades/subsistemas/meses · coloreado por '+nivelTxt.toLowerCase()+' · TOTAL opcional';
  if(showP4) sub+=' · <span style="color:'+P4C+'">▲ remates P4 activos</span>';
  return {
    title:{text:'Incidencias por unidad y mes<br><sup>'+sub+'</sup>',x:.02,font:{size:17}},
    scene:{
      domain:{x:[0,0.84],y:[0,1]},
      xaxis:{title:'Unidad',tickvals:vals,ticktext:text,backgroundcolor:'#F7F7F9',gridcolor:'#DDDDE3',zerolinecolor:'#DDDDE3'},
      yaxis:{title:'Mes',tickvals:mVals,ticktext:mText,tickfont:{size:11},backgroundcolor:'#F2F2F6',gridcolor:'#DDDDE3',zerolinecolor:'#DDDDE3'},
      zaxis:{title:'Incidencias',backgroundcolor:'#FBFBFD',gridcolor:'#DDDDE3',zerolinecolor:'#DDDDE3'},
      aspectratio:{x:1.35,y:2.25,z:.95},
      camera:{eye:{x:1.9,y:-1.9,z:.9}}
    },
    legend:{title:{text:nivelTxt+' (≥'+UMBRAL+')'},orientation:'v',itemsizing:'constant',font:{size:8},x:0.855,y:1,xanchor:'left',yanchor:'top',tracegroupgap:0,bgcolor:'rgba(255,255,255,0.85)',bordercolor:'#DDDDE3',borderwidth:1},
    paper_bgcolor:'white',
    margin:{l:0,r:8,t:58,b:18},
    font:{family:'Segoe UI, Helvetica, Arial, sans-serif',color:'#2a3f5f'}
  };
}

function clone(o){return JSON.parse(JSON.stringify(o));}
function snap(d,l,c){saved={data:clone(d),layout:clone(l),config:clone(c)};}
function bind(){gd.querySelectorAll('canvas').forEach(cv=>{if(cv.__bound)return;cv.__bound=true;cv.addEventListener('webglcontextlost',e=>{e.preventDefault();recover();},false);});}
function purge(){try{if(window.Plotly&&gd)Plotly.purge(gd);}catch(e){console.warn(e);}}
function recover(){if(!saved||recovering)return;recovering=true;setTimeout(()=>{try{purge();Plotly.newPlot(gd,saved.data,saved.layout,saved.config).then(()=>{recovering=false;bind();});}catch(e){recovering=false;console.error(e);}},250);}

// Clic en un bloque = aislar su categoría EN EL NIVEL ACTIVO (Subsistema,
// Elemento u Órgano según "Colorear por") y vuelve a dibujar con el mismo
// Plotly.react que ya usan los demás filtros. Sin añadir/quitar trazas sueltas.
function onPointClick(ev){
  if(!ev||!ev.points||!ev.points.length)return;
  const val=ev.points[0].customdata;
  if(!val)return;
  const filterId=colorBy==='organo'?'orgChecks':colorBy==='elemento'?'elemChecks':'subChecks';
  document.querySelectorAll('#'+filterId+' input[type=checkbox]:not(.grp-toggle)').forEach(x=>{x.checked=(x.value===val);});
  document.querySelectorAll('#'+filterId+' .sub-group').forEach(g=>{
    syncGroupToggle(g);
    if(g.querySelector('.sub-leaf input[type=checkbox]:checked'))g.open=true;
  });
  update();
}

// ── Undo: historial de estados de filtro ─────────────────────────────────────
function snapshotFilters(){
  function panelState(id){
    return Array.from(document.querySelectorAll('#'+id+' input[type=checkbox]:not(.grp-toggle)'))
      .map(x=>({v:x.value,c:x.checked}));
  }
  return {
    units:Array.from(document.querySelectorAll('#unitChecks input[type=checkbox]')).map(x=>x.checked),
    subs:panelState('subChecks'),
    elems:panelState('elemChecks'),
    orgs:panelState('orgChecks'),
    startMonth:document.getElementById('startMonth').value,
    endMonth:document.getElementById('endMonth').value,
    showTotal:document.getElementById('showTotal').checked,
    showTotalUnidad:document.getElementById('showTotalUnidad').checked,
    showP4:document.getElementById('showP4').checked,
    colorBy:colorBy,
  };
}
function restoreFilters(s){
  document.querySelectorAll('#unitChecks input[type=checkbox]').forEach((x,i)=>x.checked=s.units[i]);
  function restorePanel(id,arr){
    const map=Object.fromEntries(arr.map(({v,c})=>[v,c]));
    document.querySelectorAll('#'+id+' input[type=checkbox]:not(.grp-toggle)').forEach(x=>{if(x.value in map)x.checked=map[x.value];});
    document.querySelectorAll('#'+id+' .sub-group').forEach(syncGroupToggle);
  }
  restorePanel('subChecks',s.subs);restorePanel('elemChecks',s.elems);restorePanel('orgChecks',s.orgs);
  document.getElementById('startMonth').value=s.startMonth;
  document.getElementById('endMonth').value=s.endMonth;
  document.getElementById('showTotal').checked=s.showTotal;
  document.getElementById('showTotalUnidad').checked=s.showTotalUnidad;
  document.getElementById('showP4').checked=s.showP4;
  colorBy=s.colorBy;
  document.querySelector(`input[name=colorBy][value="${s.colorBy}"]`).checked=true;
  updateActivePanel();
}
function updateUndoButton(){
  const btn=document.getElementById('btnUndo');
  btn.disabled=undoStack.length===0;
  btn.title=undoStack.length>0?`Deshacer (${undoStack.length} paso${undoStack.length>1?'s':''} disponibles)`:'No hay acciones para deshacer';
}
function undoLastFilter(){
  if(!undoStack.length)return;
  restoreFilters(undoStack.pop());
  update(true);
}

function update(fromUndo=false){
  // Guardar estado anterior en el historial (salvo durante el propio deshacer
  // y la primera carga, cuando lastRenderedState aún no existe).
  if(!fromUndo && lastRenderedState){
    undoStack.push(lastRenderedState);
    if(undoStack.length>MAX_UNDO)undoStack.shift();
    updateUndoButton();
  }
  let su=selected('unitChecks'),sm=selectedMonths();
  const filterId=colorBy==='organo'?'orgChecks':colorBy==='elemento'?'elemChecks':'subChecks';
  let selF=selected(filterId);
  let totalMes=document.getElementById('showTotal').checked;
  let totalUnidad=document.getElementById('showTotalUnidad').checked;
  let showP4=document.getElementById('showP4').checked;
  if(!su.length||!selF.length||!sm.length){status.textContent='Selecciona al menos una unidad, un '+NIVEL[colorBy].singular+' y un mes.';return;}
  status.textContent='Actualizando gráfico...';
  setTimeout(()=>{
    let b=build(su,selF,sm,totalMes,showP4,totalUnidad,colorBy);
    let l=layout(b.tickVals,b.tickText,b.monthVals,b.monthText,showP4);
    let c={displaylogo:false,responsive:true,plotGlPixelRatio:1};
    snap(b.traces,l,c);
    Plotly.react(gd,b.traces,l,c).then(()=>{
      bind();
      if(!clickBound){clickBound=true;gd.on('plotly_click',onPointClick);}
      const fieldName=colorBy==='organo'?'Organo':colorBy==='elemento'?'Elemento':'Subsistema';
      let p4Count=rows.filter(r=>new Set(su).has(r.Unidad)&&new Set(selF).has(r[fieldName])&&new Set(sm).has(r.Mes)&&r.P4>0).length;
      status.textContent=`${su.length} unid., ${selF.length} ${NIVEL[colorBy].corto}, ${sm.length} meses`
        +(totalMes?', TOTAL por mes visible':'')
        +(totalUnidad?', TOTAL por unidad visible':'')
        +(showP4?` · ${p4Count} celda(s) con P4`:'')
        +` · ${b.vertices} vértices`;
      // Guardar estado recién renderizado como referencia para el próximo undo
      lastRenderedState=snapshotFilters();
      updateUndoButton();
    });
  },20);
}

document.getElementById('unitsAll').onclick=()=>setAll('unitChecks',true);
document.getElementById('unitsNone').onclick=()=>setAll('unitChecks',false);
document.getElementById('subsAll').onclick=()=>setAll('subChecks',true);
document.getElementById('subsNone').onclick=()=>setAll('subChecks',false);
document.getElementById('elemAll').onclick=()=>setAll('elemChecks',true);
document.getElementById('elemNone').onclick=()=>setAll('elemChecks',false);
document.getElementById('orgAll').onclick=()=>setAll('orgChecks',true);
document.getElementById('orgNone').onclick=()=>setAll('orgChecks',false);
document.getElementById('apply').onclick=update;
document.getElementById('btnUndo').onclick=undoLastFilter;
document.getElementById('showTotal').onchange=maybe;
document.getElementById('showTotalUnidad').onchange=maybe;
document.getElementById('showP4').onchange=maybe;
document.querySelectorAll('input[name=colorBy]').forEach(r=>r.onchange=()=>{colorBy=r.value;updateActivePanel();maybe();});
document.getElementById('startMonth').onchange=maybe;
document.getElementById('endMonth').onchange=maybe;
document.querySelectorAll('#unitChecks input').forEach(x=>x.onchange=maybe);
window.addEventListener('beforeunload',purge);
window.addEventListener('pagehide',e=>{if(e&&e.persisted)return;purge();});
updateActivePanel();
update();
})();
</script></body></html>