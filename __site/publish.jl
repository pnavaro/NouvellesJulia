using Pkg
Pkg.activate(".")
Pkg.instantiate()
Pkg.update()
using Franklin
serve(single=true)
publish()
