package commands;


import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JSlider;
import javax.swing.border.EmptyBorder;

import com.sun.speech.freetts.Voice;
import javax.swing.JLabel;

@SuppressWarnings("serial")
public class TuneAudio extends JFrame implements ActionListener{

	private JPanel panel;
	private Voice talk;
	private JSlider volumeSlider,pitchSlider;
	private JSlider rateSlider;
	private JButton ApplyButton;
	

	
	public TuneAudio(Voice talk) {
		this.talk = talk;
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		panel = new JPanel();
		panel.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(panel);
		panel.setLayout(null);
		
		JLabel volumeLabel = new JLabel("Volume:");
		volumeLabel.setBounds(57, 41, 46, 14);
		panel.add(volumeLabel);
		
		JLabel rateLabel = new JLabel("Rate:");
		rateLabel.setBounds(57, 115, 46, 14);
		panel.add(rateLabel);
		
		JLabel pitchLabel = new JLabel("Pitch:");
		pitchLabel.setBounds(57, 192, 46, 14);
		panel.add(pitchLabel);
		
		volumeSlider = new JSlider();
		volumeSlider.setBounds(180, 29, 200, 26);
		volumeSlider.setMaximum(100);
		//System.out.println((int) (talk.getVolume()*100));
		volumeSlider.setValue((int) (talk.getVolume()*100));
		panel.add(volumeSlider);
		
		
		rateSlider = new JSlider();
		rateSlider.setBounds(180, 103, 200, 26);
		rateSlider.setMinimum(100);
		rateSlider.setMaximum(200);
		rateSlider.setValue((int) talk.getRate());
		panel.add(rateSlider);
		
		
		pitchSlider = new JSlider();
		pitchSlider.setBounds(180, 180, 200, 26);
		pitchSlider.setMaximum(150);
		pitchSlider.setValue((int) talk.getPitch());
		panel.add(pitchSlider);
		
		ApplyButton = new JButton("Apply");
		ApplyButton.setBounds(335, 217, 89, 23);
		panel.add(ApplyButton);
		
		ApplyButton.addActionListener(this);
	}


	


	
	public void actionPerformed(ActionEvent e) {
		//apo8hkeuoume se ena float thn timh pou epelexe o xrhsths sto slider.
		float vol = volumeSlider.getValue()%101;
		//float rate = rateSlider.getValue();
		float pitch = pitchSlider.getValue();
		
		
		//kanoume set to volume,to rate kai to Pitch sth fwnh
		talk.setVolume(vol/100);
		//talk.setRate(rate);
		
		talk.setPitch(pitch);
		
		dispose();
		
		
		
		
		
	}
}
