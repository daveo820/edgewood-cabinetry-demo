(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const mb=$('.menu-btn'),menu=$('#menu');
if(mb){mb.addEventListener('click',()=>{const o=menu.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.textContent=o?'Close':'Menu'});
 addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.classList.contains('open')){menu.classList.remove('open');mb.setAttribute('aria-expanded',false);mb.textContent='Menu';mb.focus()}})}
// hidden door toggle on rooms.html: real before and after photos from Edgewood
$$('.secret').forEach(s=>{const b=s.querySelector('.sd-btn');b.addEventListener('click',()=>{const o=s.classList.toggle('is-open');b.setAttribute('aria-pressed',o);b.textContent=o?'Close the bookcase':'Open the bookcase'})});
// preselect from query string (?room=kitchens or ?who=builder)
const qs=new URLSearchParams(location.search);const r=qs.get('room');if(r){const i=$(`input[name=room][value="${r}"]`);if(i)i.checked=true}
const q=$('#qform');q&&q.addEventListener('submit',e=>{e.preventDefault();$('#qmsg').textContent=q.checkValidity()?'Thanks. On the live site this goes to Pete. (Demo: nothing was sent.)':'Please add your name, phone and a valid email.'});
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const count=el=>{const end=parseFloat(el.dataset.count),dec=+(el.dataset.dec||0),t0=performance.now(),d=900;const f=t=>{const k=Math.min((t-t0)/d,1),v=end*(1-Math.pow(1-k,3));el.textContent=v.toFixed(dec);if(k<1)requestAnimationFrame(f)};requestAnimationFrame(f)};
const els=$$('.rv');
if(!('IntersectionObserver' in window)||reduce){els.forEach(e=>e.classList.add('in'));return}
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){const t=en.target,s=[...t.parentNode.children].filter(x=>x.classList.contains('rv'));t.style.transitionDelay=Math.min(Math.max(s.indexOf(t),0),5)*70+'ms';t.classList.add('in');t.querySelectorAll('[data-count]').forEach(count);io.unobserve(t)}}),{rootMargin:'0px 0px -80px 0px'});
els.forEach(e=>io.observe(e));})();
