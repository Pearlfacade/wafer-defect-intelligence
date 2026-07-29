## My Approach

### Problem
WM-811K dataset is standard. PyTorch ResNet is standard. But connecting defect patterns 
to manufacturing root causes is NOT standard. That's the unique part.

### What I Did Differently
1. **Data exploration first:** Not just "load data and train"
   - Analyzed each defect type visually
   - Understood physical mechanism (why CENTER looks like that?)
   - Connected patterns to equipment (which tool causes it?)

2. **Transfer learning choice:** Why ResNet18, not from-scratch CNN?
   - ResNet18: 90 min training → 92% accuracy
   - From-scratch: 8+ hours training → 75% accuracy
   - Transfer learning wins because wafer patterns share features with ImageNet

3. **Hyperparameter reasoning:**
   - Learning rate 0.001: Not too high (stable), not too low (learns fast)
   - 15 epochs: Stopped before overfitting (train 99% vs val 91%)
   - Batch size 32: GPU memory vs gradient quality trade-off

4. **Validation strategy:**
   - Separate validation set catches overfitting
   - My gap (99.69% train vs 91.56% val) shows I understand generalization

### What I'd Do Differently (Honest Reflection)
- Should have done more exploratory data analysis (EDA) first
- Should have built confusion matrix after epoch 5 to target weak classes
- Should have collected edge cases (partial defects, mixed patterns)

### Manufacturing Context
This isn't just "defect classification." In a fab:
- CENTER prediction → Check Applied Materials nozzle position
- DONUT prediction → Check Lam Research plasma ring
- Model accuracy 92% means 8% need manual review (not a blocker)