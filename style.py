style_sheet = """
	QComboBox {
		border: 1px solid #333333;
		border-radius: 3px;
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);
		padding: 3px 30px 3px 30px;
		text-align: center;
		min-width: 4em;
		color: #ffffff;
		font-size:12px;
	}
	QComboBox:hover,
	QComboBox:focus{
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6c6c6c, stop:0.48 #5e5e5e, stop:0.52 #545454, stop:1 #474747);
	}
	QComboBox::drop-down {
		subcontrol-origin: padding;
		subcontrol-position: top right;
		width: 20px;
		text-align: center;
		border-top-right-radius: 3px;
		border-bottom-right-radius: 3px;
	}
	QComboBox::down-arrow {
		image: url(:/images/combobox-arrow.png);
	}
	
	QComboBox QAbstractView{
		background-color: #4f4f4f;
		color: #999999;
	
		selection-background-color: #999999;
		selection-color: #4f4f4f;
	}

	QPushButton {
		border: 1px solid #333333;
		border-radius: 3px;
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #797979, stop:0.48 #696969, stop:0.52 #5e5e5e, stop:1 #4f4f4f);
		padding: 4.5px 51px 4.5px 9px;
		text-align: center;
		color: #ffffff;
		font-size:12px;
	}
	QPushButton:hover,
	QPushButton:focus {
		border: 1px solid #333333;
		border-radius: 3px;
		background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6c6c6c, stop:0.48 #5e5e5e, stop:0.52 #545454, stop:1 #474747);
	}

	QScrollBar{
		width: 20px;
	}
    
    QLabel{
		background: black;
        padding: 5px 10px;
        margin-right: -5px;
	}

"""
