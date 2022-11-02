{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "efeb188c",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-11-02 19:27:39.839 INFO    numexpr.utils: Note: NumExpr detected 10 cores but \"NUMEXPR_MAX_THREADS\" not set, so enforcing safe limit of 8.\n",
      "2022-11-02 19:27:39.841 INFO    numexpr.utils: NumExpr defaulting to 8 threads.\n",
      "2022-11-02 19:27:40.531 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /Users/lorismarini/anaconda3/lib/python3.9/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "x = st.slider('x')  # 👈 this is a widget\n",
    "st.write(x, 'squared is', x * x)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
