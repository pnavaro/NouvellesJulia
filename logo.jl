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

function cocarde(fname)
    Drawing(400, 350, fname)
    origin()

    circle(O, 135, :clip)
    sethue("white")
    paint()

    sethue("blue")
    setline(10)
    circle(O, 130, :stroke)
    sethue("red")
    circle(O, 110, :stroke)

    sethue("black")
    fontface("JuliaMono-ExtraBold")
    fontsize(24)
    text("Nouvelles", Point(0, -30), halign=:center, valign=:center)
    translate(-50, -20)
    scale(0.3)
    julialogo()
    finish()
end

cocarde("logo.png")
