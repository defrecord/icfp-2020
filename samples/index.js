// Pairs 

const pair = (_first, _tail) => _f => _f(_first, _rest);
const first = _pair => _pair((_first, _tail) => _first);
const tail = _pair => _pair((_first, _tail) => _tail);


// SKI

const s = a => b => c => a(c)(d) => b(c)(d);
const k = a => b => a;
const i = a => a;


