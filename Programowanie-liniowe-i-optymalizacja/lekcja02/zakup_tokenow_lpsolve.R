install.packages('lpSolve')
require(lpSolve)
tok.direction='max'
tok.objective.in = c(500,100)
tok.const.mat = matrix(c(35,10),ncol=2)
tok.const.dir = '<='
tok.const.rhs = 100
model=lp(direction=tok.direction, 
         objective.in=tok.objective.in, 
         const.mat=tok.const.mat, 
         const.dir=tok.const.dir, 
         const.rhs=tok.const.rhs,
         all.int=TRUE)
model$solution