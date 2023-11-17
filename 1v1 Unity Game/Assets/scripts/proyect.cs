using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class proyect : MonoBehaviour {
	public float velocidad;
	AudioSource disparo;
	// Use this for initialization


	void Start () {
		velocidad = 1;
		disparo = GetComponent<AudioSource>();
		disparo.Play();

	}
	
	// Update is called once per frame
	void Update () {

		this.transform.Translate (0,0.25f,0);

		Destroy (this.gameObject, 5);
		
	}

	void OnTriggerEnter (Collider otro){
		if (otro.tag == "grounded") {
			Destroy (this.gameObject);
		}

		if (otro.tag == "hamburguesa") {
			Destroy (this.gameObject);
		
		}
	
	}


}
