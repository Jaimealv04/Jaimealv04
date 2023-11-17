using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class disparadorIzHam : MonoBehaviour {

	public GameObject bala;
	public float cadenciadisparo;
	public float siguientedisparo;
	public bool disparoerroneo;

	// Use this for initialization
	void Start () {

		cadenciadisparo = 0.5f;
		siguientedisparo = 0.5f;
		
	}
	
	// Update is called once per frame
	void Update () {

		if (Input.GetKey (KeyCode.Keypad3)) {
			disparoerroneo = true;
		}else disparoerroneo = false;

		if (Input.GetKey (KeyCode.Keypad1) && Time.time > siguientedisparo && disparoerroneo == false) {
			siguientedisparo = Time.time + cadenciadisparo;
			Instantiate (bala, this.transform.position, this.transform.rotation);

		} 
		
	}
}
