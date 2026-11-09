"""Independent checks of published aggregates; no reconstructed trial data."""
import json, math, csv
from pathlib import Path
P=Path(__file__).resolve().parent
axes=[[.060,.020,.030,.030],[.050,.060,.020,.050],[.024,.030,.024,.040]]
targets=[5,10,30,50]
rows=[]
def add(check,value,interpretation): rows.append(dict(check=check,recomputed=value,interpretation=interpretation))
for i,errors in enumerate(axes,1):
    add(f'M{i} pooled MAE mm',sum(errors)/4,'Equal n=5 per target; based on rounded table values')
    add(f'M{i} pooled MAPE percent',sum(e/t*100 for e,t in zip(errors,targets))/4,'Derived from rounded MAE and target values')
add('Overall MAE mm',sum(map(sum,axes))/12,'0.0365 rounds to 0.037 mm')
for vals in [[5.05,5.04,5.03],[10.01,10.02,10.04],[20.04,19.98,19.97],[30.01,30.02,30.02]]:
    add('Synchronized spread '+str(vals),max(vals)-min(vals),'End-point spread only; not dynamic synchrony')
add('Pulses per mm',200*16/4,'Command conversion; not physical accuracy')
add('Increment mm',4/(200*16),'Caliper display resolution is 8 command increments')
for rate in [.1,1,3,10]: add(f'Pulse interval seconds at {rate} mm/day',86400/(rate*800),'Reference mechanics')
add('Mixed microstep displacement mm',80/800+80/50,'1.7 mm')
add('Maximum schedule deviation percent',.002/60*100,'0.003333 percent; below nominal timebase uncertainty')
add('Nominal 50 ppm uncertainty at 60s in ms',50e-6*60*1000,'3 ms; nominal spec not calibration certificate')
add('p95 difference ms',15.152925-14.906705,'Cross-run difference; insufficient to establish within-run drift')
add('p95 relative difference percent',(15.152925/14.906705-1)*100,'Approximately 1.65 percent')
add('Requests per second over soak',717/3600,'Approximately 0.199; not saturation throughput')
add('Oblique vector norm mm',math.hypot(30,30),'42.4264069 mm')
add('Complication TP FN TN FP','0 1 14 0','Inferred from n=15, one positive, sensitivity 0, specificity 1')
add('Complication accuracy',14/15,'Same as all-negative baseline')
add('Complication balanced accuracy',(.0+1)/2,'0.5 at threshold 0.5')
add('Sensitivity exact two-sided 95 percent CI','[0, 0.975]','Clopper-Pearson for 0/1')
add('Specificity exact two-sided 95 percent lower bound',.025**(1/14),'Upper bound 1; 14/14 negatives')
for n in [200,717]:add(f'One-sided 95 percent failure upper bound 0/{n}',1-.05**(1/n),'Independent identically distributed Bernoulli assumption; not device reliability')
add('Default candidate rates',[2.8,2.9,3,3.1,3.2],'All outside synthetic training interval [0.55,1.55]')
with (P/'calculation_checks.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
print(json.dumps(rows,indent=2))
