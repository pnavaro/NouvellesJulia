using Luxor

# @svg begin
#     sethue(Luxor.julia_blue)
#     setline(8)
#     circle(Point(0,0), 200, :stroke)
#     juliacircles()
#     sethue("white")
#     setfont("JuliaMono", 55)
#     points = ngon(0, 0, 100, 3, pi/6, vertices=true)
#     settext.(["f", "f", "uj"], points; markup=true, halign = "center", valign = "center")
# 
# 
# end

function create_logo(fname)
    Drawing(200, 150, fname)
    origin()

    sethue("black")
    fontface("JuliaMono-ExtraBold")
    fontsize(24)
    text("Nouvelles", Point(0, -50), halign=:center, valign=:center)
    translate(-70, -50)
    scale(0.5)
    julialogo()
    finish()
end

create_logo("logo.png")
