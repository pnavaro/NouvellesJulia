using Pkg
Pkg.activate(".")
Pkg.instantiate()
Pkg.update()
using Franklin
using NodeJS
run(`$(npm_cmd()) install -g npm`);
run(`$(npm_cmd()) install highlight.js`);
serve(single=true)
optimize()
publish()
