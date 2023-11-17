using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class puntiMedioCamaras : MonoBehaviour {
	public GameObject mapa;
	GameObject Samu;
	GameObject Ham;
	public float factor;

	// Use this for initialization
	void Start () {
		Samu = GameObject.Find("MonopatinSamurai");
		Ham = GameObject.Find("personajeanimado");
	}
	
	// Update is called once per frame
	void Update () {
		factor = (Samu.transform.position - Ham.transform.position).magnitude;
		if(factor < 3.00f){
			factor = 3.00f;
		}
		if(factor > 12.00f){
			factor = 12.00f;
		}
		this.transform.position = (Samu.transform.position + Ham.transform.position)*0.5f;
		mapa.GetComponent<Camera>().fieldOfView = 3.00f*factor;
	}
}
