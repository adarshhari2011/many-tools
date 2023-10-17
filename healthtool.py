def bmi(kg,m):
  return (kg)/m*m
def lb_to_kg(lb):
  return lb*0.453592
def kg_to_lb(kg):
  return kg*2.20462
def cm_to_in(cm):
  return cm*0.393701
def in_to_cm(inch):
  return inch*2.54
def blood_pressure_high_low(bp):
  if bp<120:
    return "Low"
  elif bp>=120 and bp<=129:
    return "Normal"
  elif bp>=130 and bp<=139:
    return "Pre-high"
  elif bp>=140 and bp<=180:
    return "High"
  else:
    return "Very high"