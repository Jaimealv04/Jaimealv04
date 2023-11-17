using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class proyectilGordo : MonoBehaviour {

	public float velocidad;
	AudioSource disparohamburguesa;

	// Use this for initialization
	void Start () {

		velocidad = 0.5f;
		disparohamburguesa = GetComponent<AudioSource>();
		disparohamburguesa.Play();
		
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

		if (otro.tag == "samurai") {
			Destroy (this.gameObject,4);

		}

	}
}
