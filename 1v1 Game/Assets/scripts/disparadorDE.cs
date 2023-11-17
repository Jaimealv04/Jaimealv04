using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class disparadorDE : MonoBehaviour {
//	public GameObject lanzallamas;
	public GameObject bala;
	public float cadenciadisparo;
	public float siguientedisparo;
	public bool disparoerroneo;
//	public bool Lanzallamas;

	// Use this for initialization
	void Start () {
//		Lanzallamas = false;
		cadenciadisparo = 0.5f;
		siguientedisparo = 0.5f;
		
	}
	
	// Update is called once per frame
	void Update () {

		if (Input.GetKey ("f")) {
			disparoerroneo = true;
		} else disparoerroneo = false;
		
		if (Input.GetKey ("h") && Time.time > siguientedisparo && disparoerroneo == false ) {
			siguientedisparo = Time.time + cadenciadisparo;
			Instantiate (bala, this.transform.position, this.transform.rotation);
		
		}
		
		/*if (Lanzallamas == true){
			Instantiate(lanzallamas, this.transform.position, this.transform.rotation);
		}*/
	}
/*
	void OnTriggerEnter(Collider otro){
    if (otro.tag == "lanzallamas" && Input.GetKey("h")) {	
		Lanzallamas = true;
			
		}
	}*/
	
}
