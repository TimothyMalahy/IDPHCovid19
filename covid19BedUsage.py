import plotly.graph_objects as go

bedsTotal = 3820
bedsUsed = 3820-1734
bedsAvail = 1734

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = bedsUsed,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "ICU Bed Usage", 'font': {'size': 36}},
    #delta = {'reference': bedsAvail, 'increasing': {'color': "RebeccaPurple"}},
    gauge = {
        'axis': {'range': [None, 3820], 'tickwidth': 1, 'tickcolor': "darkblue"},
        'bar': {'color': "#607d8b"},
        'bgcolor': "white",
        'borderwidth': 7,
        'bordercolor': "gray",
        'steps': [
            {'range': [.70*bedsTotal, bedsTotal], 'color': '#f44336'},
            {'range': [.50*bedsTotal, .70*bedsTotal], 'color': '#ffeb3b'},
            {'range': [0,.50*bedsTotal], 'color':'#4caf50'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': bedsUsed}}))

fig.update_layout(paper_bgcolor = "white", font = {'color': "darkblue", 'family': "Arial"})

fig.show()
